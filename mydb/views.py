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
    result={"code":0,"msg":"查询失败","data":[]}#0表示失败，1表示成功
    '''if all_information==None:
        result['code']=0
        result['msg']="查询失败"'''
    if len(all_information)==0:
        result['code']=0#0表示失败
        result['msg']="查询失败"
    else:
        result['code']=1#1表示成功
        result['msg']="查询成功"
        i=0
        for item in all_information:
            if i>=15:
                break
            i+=1
            '''result["data"].append({"room":item['roomId'],"roomType":item['roomType'],"date":item['date'],
                                   "timeslot":item['time'],"status":item['status']})'''
            result["data"].append({"room":item.roomId,"roomType":item.roomType,"date":item.date,
                                   "timeslot":item.time,"status":item.status})
    Jsondata=json.dumps(result)
    #Jsondata是返回的Json数据
    return HttpResponse(Jsondata,content_type='application/json')
#前端还是用post方法！
def get_appointment(request):
    all_information = models.rooms_teacher.objects.filter(status=2)#2代表待处理
    result = {"code": 0, "msg": "查询失败", "data": []}#0表示失败，1表示成功
    '''if all_information==None:
        result['code'] = 0
        result['msg'] = "查询失败"'''
    if len(all_information)==0:
        result['code']=0#0表示失败
        result['msg']="查询失败"
    else:
        result['code']=1
        result['msg']="查询成功"
        for item in all_information:
            '''result["data"].append({"workNum":item['teacherId'],"teacherName":item['name'],"roomType":item['roomType'],
                                   "roomId":item['roomId'],"date":item['date'],"timeslot":item['time']})'''
            result["data"].append(
                {"workNum": item.teacherId, "teacherName": item.name, "roomType": item.roomType,
                 "roomId": item.roomId, "date": item.date, "timeslot": item.time})
    Jsondata=json.dumps(result)
    #Jsondata是返回的Json数据
    return HttpResponse(Jsondata,content_type='application/json')
def meetingRoomAppointment(request):
    body=request.body
    data=json.loads(body)
    teacherId=data['teacherId']
    roomId=data['roomId']
    date=data['date']
    time=data['time']
    
    result = {}
    SuccessResult = {"code": 1, "msg": "预约成功", "data": []}
    FailedResult = {"code": 0, "msg": "预约失败", "data": []}
    
    #查询teacherId 所对应的name
    if models.teacher.objects.filter(teacherId = teacherId).count()!=1:
        result = FailedResult
    else:
        
        name = models.teacher.objects.filter(teacherId = teacherId)[0].name
        #判断会议室是否已被占用
        #roomType 1代表会议室，2代表实验室
        if models.rooms_teacher.objects.filter(roomType=1,date=date,time=time).count()==0:
            models.rooms_teacher.objects.create(roomId=roomId,teacherId=teacherId,name=name,roomType=1,date=date,time=time,status=0)
            result = FailedResult   
        else: 
            models.rooms_teacher.objects.create(roomId=roomId,teacherId=teacherId,name=name,roomType=1,date=date,time=time,status=1)
            result = SuccessResult 
               
    #Jsondata是返回的Json数据
    Jsondata=json.dumps(result)    
    return HttpResponse(Jsondata,content_type='application/json')

def checkWorkNumber(request):
    body = request.body
    data = json.loads(body)
    nickName = data['nickName']
    all_information=models.teacher.objects.filter(weChatId=nickName)
    results={"code": 1, "msg": "查询成功", "data": []}
    if len(all_information) == 0:
        results['code'] = 0
        results['msg'] = "无工号"
    else:
        results['code'] = 1
        results['msg'] = "查询成功"
        for item in all_information:
            results["data"].append({"workNum":item.teacherId})
    Jsondata = json.dumps(results)
    return HttpResponse(Jsondata,content_type='application/json')

def insertRecord(request):
    body = request.body
    data = json.loads(body)
    nickName = data['nickName']
    workNum = data['workNum']
    results = {"code": 1, "msg": "绑定成功"}
    #查看此nickName是否绑定了工号，若已绑定则返回“插入失败”
    checkNum = models.teacher.objects.filter(weChatId=nickName)
    #checkNum不为空，说明已绑定过工号
    if len(checkNum) != 0:
        results['code'] = 0
        results['msg'] = "插入失败"
    else:
        #checkNum为空，无绑定记录，则插入一条绑定工号记录
        t1 = models.teacher(teacherId=workNum, weChatId=nickName)
        t1.save()
        #另外一种插入方式
        #models.teacher.objects.create(teacherId=workNum, weChatId=nickName)
        #查询是否成功插入
        all_information = models.teacher.objects.filter(weChatId=nickName, teacherId=workNum)
        if len(all_information) == 0:
            results['code'] = 0
            results['msg'] = "插入失败"
        else:
            results['code'] = 1
            results['msg'] = "绑定成功"
    Jsondata = json.dumps(results)
    return HttpResponse(Jsondata, content_type='application/json')

def deleteRecord(request):
    body = request.body
    data = json.loads(body)
    nickName = data['nickName']
    results = {"code": 1, "msg": "删除成功"}
    checkRecord = models.teacher.objects.filter(weChatId=nickName)
    #如果找不到记录，则无需删除，返回删除失败
    if len(checkRecord) == 0:
        results['code'] = 0
        results['msg'] = "删除失败"
    else:
        #找得到记录，删除记录
        #checkRecord.delete()
        models.teacher.objects.filter(weChatId=nickName).delete()
        #检查是否删除成功
        all_information = models.teacher.objects.filter(weChatId=nickName)
        if len(all_information) == 0:
            results['code'] = 1
            results['msg'] = "删除成功"
        else:
            results['code'] = 0
            results['msg'] = "删除失败"
    Jsondata = json.dumps(results)
    return HttpResponse(Jsondata, content_type='application/json')