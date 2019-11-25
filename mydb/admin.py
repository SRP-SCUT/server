from django.contrib import admin
from mydb.models import teacher
from mydb.models import rooms_teacher
from mydb.models import rooms
from mydb.model_admin import RoomsTeacherAdmin
from mydb.model_admin import RoomAdmin
from mydb.model_admin import TeacherAdmin

admin.site.site_header='实验室预约后台管理系统'
admin.site.site_title='实验室预约系统'


admin.site.register(teacher,TeacherAdmin)
admin.site.register(rooms_teacher,RoomsTeacherAdmin)
admin.site.register(rooms,RoomAdmin)
# Register your models here.
