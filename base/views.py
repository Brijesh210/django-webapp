from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
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
    issues = Issue.objects.all()

    context = {'user': user,
    'issues': issues}
    return render(request, "base/home.html", context)


def userRegisterPage(request):

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreateForm()

    return render(request, 'base/forms/user_register_form.html', {'form': form})


def addressRegisterPage(request):

    if request.method == 'POST':
        form = AddressCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddressCreateForm()

    return render(request, 'base/forms/address_register_form.html', {'form': form})


def propertyRegisterPage(request):
    user = request.user

    if request.method == 'POST':
        form = PropertyCreateForm(request.POST)
        if form.is_valid():
            addOwnerId = form.save(commit=False)
            addOwnerId.ownerId = user
            addOwnerId.save()
            form.save_m2m()

            return redirect('home')
    else:
        form = PropertyCreateForm()

    return render(request, 'base/forms/property_register_form.html', {'form': form})


def issueCategoryRegisterPage(request):

    if request.method == 'POST':
        form = IssueCategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IssueCategoryCreateForm()

    return render(request, 'base/forms/issue_category_register_form.html', {'form': form})



def issueRegisterPage(request):
    user = request.user.id

    if request.method == 'POST':
        form = IssueCreateForm(request.POST)
        if form.is_valid():
            addSubmiterId = form.save(commit=False)
            addSubmiterId.submitter_id = user
            addSubmiterId.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = IssueCreateForm()

    return render(request, 'base/forms/issue_create_form.html', {'form': form})



def issueUpdatePage(request):
    user = request.user.id

    if request.method == 'POST':
        form = IssueCreateForm(request.POST)
        if form.is_valid():
            addSubmiterId = form.save(commit=False)
            addSubmiterId.submitter_id = user
            addSubmiterId.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = IssueCreateForm()

    return render(request, 'base/forms/issue_create_form.html', {'form': form})


def updateManagerIssue(request,pk):
    issues = Issue.objects.all()
    print(pk)
    if request.method == 'POST':
        form = IssueUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IssueUpdateForm()

    context = {'issues': issues,
                'form': form}
    return render(request, 'base/home.html', context)
