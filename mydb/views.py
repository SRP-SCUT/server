from django.shortcuts import render
from mydb import models
import json
from django.shortcuts import HttpResponse
# Create your views here.
def get_history(request):
    body=request.body
    # print(body)
    data=json.loads(body)
    nickName=data['nickName']
    workNum=data['workNum']
    all_information=models.rooms_teacher.objects.filter(teacherId=workNum)
    result={"code":1,"msg":"查询失败","data":[]}
    if all_information==None:
        result['code']=1
        result['msg']="查询失败"
    else:
        result['code']=0
        result['msg']="查询成功"
        i=0
        for item in all_information:
            if i>=15:
                break
            i+=1
            result["data"].append({"room":item['roomId'],"roomType":item['roomType'],"date":item['date'],
                                   "timeslot":item['time'],"status":item['status']})
        Jsondata=json.dumps(result)
        #Jsondata是返回的Json数据
        return HttpResponse(Jsondata,content_type='application/json')
#前端还是用post方法！
def get_appointment(request):
    all_information = models.rooms_teacher.objects.filter(status=2)#2代表待处理
    result = {"code": 1, "msg": "查询失败", "data": []}
    if all_information==None:
        result['code'] = 1
        result['msg'] = "查询失败"
    else:
        result['code']=0
        result['msg']="查询成功"
        for item in all_information:
            result["data"].append({"workNum":item['teacherId'],"teacherName":item['name'],"roomType":item['roomType'],
                                   "roomId":item['roomId'],"date":item['date'],"timeslot":item['time']})
        Jsondata=json.dumps(result)
        #Jsondata是返回的Json数据
        return HttpResponse(Jsondata,content_type='application/json')
# Create your views here.
