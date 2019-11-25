from django.contrib import admin

class RoomsTeacherAdmin(admin.ModelAdmin):
    list_display = ('roomId', 'name', 'teacherId', 'date', 'time', 'status_view')
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
    actions = [accept_satus,reject_status]