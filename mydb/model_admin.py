from django.contrib import admin
from mydb.models import rooms_teacher
from mydb.models import teacher

class RoomsTeacherAdmin(admin.ModelAdmin):
    fields = ('roomId','name','teacherId','date','time','status')
