# djago Server

## 1. 运行

安装依赖：

> pip install -r requirements.txt

配置数据库：

请确保你已安装mysql，删除 mydb/migrations/0001_initial.py ，更改srpProgram/settings.py 中的 Database，将其中的userName和passWord更改为你自己的，并运行

> python manage.py makemigrations mydb
>
> python manage.py migrate mydb

## 2. 开发

1. 请严格按照路由跳转原则开发。即用到的函数均需要在 srpProgram/urls.py 中注明，如前端发送Post 请求到 Path：/user/history，且这个请求由mydb/views.py中的get_history函数处理，则urlpatters如下形式：

   ```python
   from mydb import views
   from django.urls import path
   
   urlpatterns = [
       path('user/history', views.get_history)
   ]
   ```

   切记要一一对应，将你写有处理函数的py文件import进来

2. 因为前端发送数据为Json格式的字符串，所以后端解析数据是需要用 json 模块解析字符串，具体形式如下

   ```python
   #获取数据字符串
   body=request.body
   #解析字符串得到数据，数据此时为字典格式
   data=json.loads(body)
   #以字典形式读取其中各个键值数据
   nickName=data['nickName']
   workNum=data['workNum']
   ```

3. > roomType: 0 : meetingRoom, 1 : labroom
   >
   > status: 0: 拒绝，1：预约成功，2：待定

    


## 3. API 细节

```javascript
path：user/meetingRoom/checkTime
method：Post
data：{
roomNum
date：
}
//后端需要在数据库中查roomNum对应date的那些时间段已经被预约了，吧已预约的时间段返回给我
{
code： 0/1
msg：'查询失败/成功'
data:{
[]//(已预约的时间段列表）
}
}


```



历史预约页面：

```javascript
PATH：/user/history
method: POST
data: {
nickName: '',
workNum: ''
}
//你使用workNum到数据库查询这个workNum对应的预约记录，返回前15条
//返回数据:
{
code: 0/1,  (代表成功/失败）
msg: "查询成功/失败",
data: 一个数组，每一个item包括：{
room: "",
roomType: "",
date: "",
timeslot: "",
status: ""
}
}
```

插入记录(绑定工号):

```javascript
path: user/signup
data:{
nickName:
workNum:
}
//向数据库插入一条记录，teacherId值为workNum，wechatId值为nickName，插入成功后返回{
code：1
msg： '绑定成功'
}
否则失败的话返回
{
code：0,
msg: '插入失败'
}
```

