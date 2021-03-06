"""srpProgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from mydb import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/history', views.get_history),
    path('appointment',views.get_appointment),
    path('user/meetingRoom/order',views.meetingRoomAppointment),
    path('user/login', views.checkWorkNumber),
    path('user/signup',views.insertRecord),
    path('user/unbind', views.deleteRecord),
    path('user/meetingRoom/checkTime',views.meetingRoomCheck),
    path('user/labRoom/checkTime',views.labRoomCheck),
    path('user/labRoom/order',views.labRoomAppointment),
]
