from django.contrib import admin
from mydb.models import teacher
from mydb.models import rooms_teacher
from mydb.models import rooms
from mydb.model_admin import RoomsTeacherAdmin

admin.site.register(teacher)
admin.site.register(rooms_teacher,RoomsTeacherAdmin)
admin.site.register(rooms)
# Register your models here.
