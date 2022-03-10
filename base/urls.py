from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home , name="home"),
    path('login/', views.loginPage , name="loginPage"),
    path('logout/', views.logoutPage , name="logoutPage"),
    path('userRegisterPage/', views.userRegisterPage , name="userRegisterPage"),
    path('addressRegisterPage/', views.addressRegisterPage , name="addressRegisterPage"),
    path('propertyRegisterPage/', views.propertyRegisterPage , name="propertyRegisterPage"),
    # path('register/owner', views.ownerRegisterPage , name="ownerRegisterPage"),
    # path('register/tenant', views.tenantRegisterPage , name="tenantRegisterPage"),
    # path('roomForm/', views.roomForm , name="roomForm"),
    # path('issueForm/', views.issueForm , name="issueForm"),
]
