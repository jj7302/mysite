from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Voulunteer_Event, User
from .forms import NewUserForm, HourForm
from django.contrib import messages
from django.utils import timezone
# Create your views here.


class member_info():
    def __init__(self, username='', events=[], hours=0):
        self.username = username
        self.events = events
        self.hours = hours
        self.link = "/individual-hours/" + self.username



def home(request):
    return render(request=request,
                template_name="main/home.html")


def check_individual_hours(request, username):
    user = User.objects.all().filter(username=username).first()
    return render(request=request,
                  template_name="main/check-individual-hours.html",
                  context={"events": Voulunteer_Event.objects.all().filter(user=user)}
                  )


def check_hours(request):
    member_information = []
    for usr in User.objects.all():
        events = Voulunteer_Event.objects.all().filter(user=usr)
        total_hours = 0
        for evnt in events:
            total_hours += evnt.hours
        member_information.append(member_info(username=usr.username, events=events, hours=total_hours))

    return render(request=request,
                template_name="main/check-hours.html",
                context={"members": member_information})

def log_hours(request):
    if request.method == "POST":
        form = HourForm(request.POST)
        if form.is_valid():
            eventName = form.cleaned_data.get('event_name')
            post = form.save(commit=False)
            post.user = request.user
            post.date = timezone.now()
            post.save()
            messages.success(request, "Event Successfully Added: " + str(eventName))
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, str(msg) + ": " + str(form.error_messages[msg]))


    form = HourForm
    return render(request,
                  "main/log-hours.html",
                  context={"form": form})

def view_hours(request):
    events = Voulunteer_Event.objects.all().filter(user=request.user)
    total = 0
    for event in events:
        total += event.hours
    return render(request,
                  "main/view-hours.html",
                  context={"events": events, "total": total})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "New Account Created: " + str(username))
            login(request, user)
            messages.info(request, "You are now logged in as " + str(username))
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, str(msg) + ": " + str(form.error_messages[msg]))

    form = NewUserForm
    return render(request,
                  "main/register.html",
                  context={"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged Out Successfully")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as " + str(username))
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request, "main/login.html", {"form": form})

