from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from .forms import MyUserCreationForm


# Create your views here.

def home(request):
    return render(request, 'base/home.html')


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('loginPage')
        else:
            messages.error(request, "usernaem or Password dosen't exist")

    context = {'page': page}

    return render(request, 'base/login_page.html', context)


def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def registerPage(request):

    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit="False")
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Something went wrong with registraion")

    context = {'form': form}
    return render(request, 'base/login_page.html', context)