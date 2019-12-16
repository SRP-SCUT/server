from django.contrib import admin

class RoomsTeacherAdmin(admin.ModelAdmin):
    list_display = ('roomId', 'name', 'teacherId', 'date', 'time_slot', 'status_view')

    meetingRoom= [{
        'title': '第一节(9:00-10.30)',
        'value': '0',
    },
        {
            'title': '第二节(10:30-12:00)',
            'value': '1',
        },
        {
            'title': '第三节(14:00-15:30)',
            'value': '2',
        },
        {
            'title': '第四节(15:30-17:00)',
            'value': '3',
        },
        {
            'title': '第五节(18:30-20:00)',
            'value': '4',
        },
        {
            'title': '第六节(20:00-21:30)',
            'value': '5',
        },
        {
            'title': '第七节(21:30-23:00)',
            'value': '6',
        },
        {
            'title': '整天',
            'value': 'full'
        }],
    labRoom=[
        {
            'title': '第一小节课',
            'value': '0',
        },
        {
            'title': '第二小节课',
            'value': '1',
        },
        {
            'title': '第三小节课',
            'value': '2',
        },
        {
            'title': '第四小节课',
            'value': '3',
        },
        {
            'title': '第五小节课',
            'value': '4',
        },
        {
            'title': '第六小节课',
            'value': '5',
        },
        {
            'title': '第七小节课',
            'value': '6',
        },
        {
            'title': '第八小节课',
            'value': '7',
        },
        {
            'title': '第九小节课',
            'value': '8',
        },
        {
            'title': '第十小节课',
            'value': '9',
        },
        {
            'title': '第十一小节课',
            'value': '10',
        },
        {
            'title': '第十二小节课',
            'value': '11',
        },
        {
            'title': '整天',
            'value': 'full',
        }]

    def time_slot(self,obj):
        result=''
        timeslots=obj.time.split(',')
        meetingRoom=self.meetingRoom[0]
        labRoom=self.labRoom
        for time in timeslots:
            if obj.roomType==0:
                for i in range(len(meetingRoom)):
                    option=meetingRoom[i]
                    if time==option['value']:
                        result+=option['title']+','
            elif obj.roomType==1:
                for i in range(len(labRoom)):
                    option=labRoom[i]
                    if time==option['value']:
                        result+=option['title']+','
        return result

    def status_view(self,obj):
        if obj.status==2:
            return '待定'
        elif obj.status==0:
            return '拒绝'
        elif obj.status==1:
            return '接受'
    def accept_satus(self,request,queryset):
        queryset.update(status=1)
    accept_satus.short_description = '批量接受'

    def reject_status(self,request,queryset):
        queryset.update(status=0)
    reject_status.short_description = '批量拒绝'

    list_filter = ('status',)
    ordering = ('-date',)
    search_fields = ['status','name','roomId']
    list_editable = ['teacherId','name']
    actions = [accept_satus,reject_status]
    list_per_page = 50

class RoomAdmin(admin.ModelAdmin):
    list_display = ('roomId','maxCap','view_room_type')
    def view_room_type(self,obj):
        if obj.roomType==0:
            return '会议室'
        elif obj.roomType==1:
            return '实验室'
    list_filter = ('roomType',)
    ordering = ('roomId',)
    list_editable = ['maxCap']

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacherId','weChatId','name')
    ordering = ('name',)
    list_editable = ['name','weChatId']
