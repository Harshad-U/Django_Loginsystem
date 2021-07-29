from django.shortcuts import render
from django.contrib.auth.models import  auth
from django.views.decorators.csrf import  csrf_exempt
from django.contrib.auth.models import User
from .models import UserSystem
from django.http import  HttpResponse


import random

# Create your views here.
def home(request):
    if request.method == 'POST':
        username  = request.POST['uname']
        password  = request.POST['pass']
        user  = auth.authenticate(username= username,password= password)
        if user is not  None:
            return  render(request,"home/welcome.html")
        else:
            return render(request, "home/home.html")
    return render(request, "home/home.html")
def register(request):

    if request.method=='POST':
        firstname = request.POST.get("fname")
        lastname = request.POST.get("lname")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip = request.POST.get("zip")
        mail = request.POST.get("mail")
        mobile = request.POST.get("mobile")
        user = request.POST.get("uname")
        pwd= request.POST.get("pass1")
        userreg = User(username = user)
        userreg.set_password(pwd)
        userreg.save()
        usersys = UserSystem(user = userreg,firstname = firstname,lastname = lastname,city = city,state = state,zip = zip, email = mail, mobile = mobile)
        usersys.save()
        return render(request, "home/home.html")
    num = random.randrange(1121, 9899)
    global str_num
    str_num=str(num)
    return render(request, 'home/register.html',{"captcha": str_num})

@csrf_exempt
def welcome(request):
    return render(request, "home/welcome.html")

@csrf_exempt
def logout(request):
    auth.logout(request)
    return render(request,'home/home.html')