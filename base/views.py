from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from .forms import *


def loginPage(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")
        print(password)


        try:
            user = User.objects.get(email=email)

        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "username or Password dosen't exist")

    context = {"page": page}
    return render(request, "base/login_page.html", context)


def logoutPage(request):
    logout(request)
    return redirect('loginPage')


@login_required(login_url="loginPage")
def home(request):
    user = request.user
    context = {'user': user}
    return render(request, "base/home.html", context)


def userRegisterPage(request):

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreateForm()

    return render(request, 'base/user_register_form.html', {'form': form})

