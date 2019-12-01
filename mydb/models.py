from django.db import models

# Create your models here.
class teacher(models.Model):
    id = models.AutoField
    teacherId = models.CharField(null=False,max_length=80)
    weChatId = models.CharField(null=False,max_length=80)
    name = models.CharField(null=False,default="NoUserNick",max_length=255)
    class Meta:
        #managed = False
        db_table = 'teacher'


class rooms(models.Model):
    id = models.AutoField
    roomId = models.CharField(null=False,max_length=80)
    maxCap = models.IntegerField(null=False,default=0)
    roomType = models.IntegerField(null=False,default=0)
    class Meta:
        #managed = False
        db_table = 'rooms'

class rooms_teacher(models.Model):
    id = models.AutoField
    roomId = models.CharField(null=False,max_length=80)
    teacherId = models.CharField(null=False,max_length=80)
    name = models.CharField(null=False, default="NoUserNick", max_length=255)
    date =  models.CharField(null=False,max_length=80)
    time =  models.CharField(null=False,max_length=80)
    roomType = models.IntegerField(null=False, default=0)
    status=models.IntegerField(null=False, default=2)
    class Meta:
        #managed = False
        db_table = 'rooms_teacher'
