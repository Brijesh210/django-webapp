from collections import namedtuple
from statistics import mode
from typing import ContextManager, FrozenSet
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from django.db.models import Q


def home(request):
    user = request.user
    context = {'user': user}
    return render(request, "base/home.html", context)



# @login_required(login_url="loginPage")
# def home(request):

#     user = request.user
#     if user.is_owner == True:
#         rooms = Room.objects.filter(owner=user.owner)
#         issues = Issue.objects.filter(room__in=rooms)
#         tenants = Tenant.objects.filter(owner=user.owner)
#         owners = ''

#     if user.is_tenant == True:
#         owners = Owner.objects.all()

#         rooms = ''
#         issues = ''
#         tenants = ''
#         # rooms = Room.objects.filter(tenant = user.tenant)

#     else:
#         rooms = ''
#         issues = ''
#         tenants = ''
#         owners = ''

#     # issues = Issue.objects.filter(room__in=rooms)

#     # tenants = Tenant.objects.filter(id = user.id)
#     # print(tenants)

#     context = {'user': user, 'rooms': rooms,
#                'issues': issues, 'tenants': tenants, 'owners': owners}
#     return render(request, "base/home.html", context)


def loginPage(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")

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
    return redirect('home')


# def registerPage(request):

#     page = "signup"
#     context = {"page": page}

#     return render(request, "base/register_page.html", context)


# def ownerRegisterPage(request):
#     page = "ownerSignup"
#     form = OwnerForm()

#     if request.method == "POST":
#         form = OwnerForm(request.POST)

#         if form.is_valid():
#             user = form.save(commit="False")
#             user.username = user.username.lower()
#             user.is_owner = True
#             owner = Owner(user=user)
#             owner.save()
#             user.save()
#             login(request, user)
#             return redirect("home")
#         else:
#             messages.error(request, "Something went wrong with registraion")

#     context = {"form": form, "page": page}
#     return render(request, "base/register_page.html", context)


# def tenantRegisterPage(request):
#     page = "tenantSignup"
#     form = TenantForm()

#     if request.method == "POST":
#         form = TenantForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit="False")
#             user.is_tenant = True
#             user.save()

#             login(request, user)
#             return redirect("home")
#         else:
#             messages.error(request, "Something went wrong with registraion")

#     context = {"form": form, "page": page}
#     return render(request, "base/register_page.html", context)


# @login_required(login_url="loginPage")
# def roomForm(request):
#     form = RoomForm()

#     if request.method == "POST":
#         Room.objects.create(
#             name=request.POST.get('name'),
#             address=request.POST.get('address'),
#             owner=Owner.objects.get(user=request.user),
#             tenant = request.POST.get('tenant')
#         )

#         return redirect("home")

#     context = {"form": form}
#     return render(request, "base/room_form.html", context)


# def issueForm(request):
#     form = IssueForm()
#     user = request.user

#     if request.method == "POST":

#         owner = Owner.objects.get(id=request.POST.get('owner'))
        
#         tenant = Tenant(
#             user = user, owner = owner 
#         )
#         tenant.save()
       

#         room = Room.objects.get(id=request.POST.get('room'))
#         room.tenant = tenant
#         room.save()
#         print (room)
#         # owner = Tenant(owner = request.POST.get('owner'))
#         Issue.objects.create(
#             owner=owner,
#             tenant=tenant,
#             name=request.POST.get("name"),
#             room=room,
#             description=request.POST.get("description"),
#         )
#         return redirect("home")

#     context = {"form": form, }
#     return render(request, "base/issue_form.html", context)
