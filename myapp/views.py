from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignUpForm, AddForm
from .models import Record


def home_view(request):
    records = Record.objects.all()
    return render(request, 'home.html', {'records': records})


def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in (^^)')
            return redirect('home')
        else:
            messages.error(request, 'wrong username or password :(')
            return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You are logged out (^^)')
    return redirect('login')


def signup_view(request):
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'you are signed up (^^)')
            return redirect('home')
        else:
            messages.success(request, 'wrong username or password :(')
            return render(request, 'signup.html', {'form': form})


def record_view(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(pk=pk)
        return render(request, 'record.html', {'record': record})
    else:
        messages.error(request, 'login first (^^)')
        return redirect('login')


def delete_view(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(pk=pk)
        record.delete()
        messages.success(request, 'Record deleted successfully (^^)')
        return redirect('home')
    else:
        messages.success(request, 'something went wrong :(')
        return redirect('record', pk)


def edit_view(request, pk):
    if request.user.is_authenticated:

        record = Record.objects.get(pk=pk)
        form = AddForm(request.POST or None, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record edited successfully (^^)')
            return redirect('home')

        return render(request, 'edit.html', {'form': form})
    else:
        messages.success(request, 'Login first :(')
        return redirect('home')


def add_view(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = AddForm()
            return render(request, 'add.html', {'form': form})
        if request.method == 'POST':
            form = AddForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Record added successfully (^^)')
                return redirect('home')
    else:
        messages.success(request, 'Login first :(')
        return redirect('home')

