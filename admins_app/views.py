import hashlib
import os
import random
import string
import traceback

import re
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from admins_app.models import User
from admins_app.tools.image import ImageCaptcha


def getSalt():
    l='!@#$%^&*()_+/.,?><";:'
    salts="".join(random.sample(l,5))
    print(salts)
    return salts

def register_page(request):
    #跳转模板
    return render(request,'admins_app/register.html')

def register_logic(request):
    #收参
    ceilphone=request.POST.get('txt_username')

    txt_password=request.POST.get('txt_password')

    salts=getSalt()
    h=hashlib.md5()
    password=salts+txt_password
    h.update(password.encode())
    passwords=h.hexdigest()

    try:
        with transaction.atomic():
            user=User(ceilphone=ceilphone,password=passwords,salts=salts,user_status=1)
            user.save()
            request.session['user_id']=user.id
            request.session['ceilphone']=ceilphone
            request.session['user_status']=1
            car=request.session.get('car')
            if car:
                return redirect('shop:paypage')
            return redirect('user:register:ok')
    except:

        traceback.print_exc()

        return redirect('user:register:page')

def register_ok(request):

    return render(request,'admins_app/registerok.html')


def login_page(request):

    return render(request,'admins_app/login.html')

def login_logic(request):

    val1 = request.GET.get('val1')
    val2 = request.GET.get('val2')


    user = User.objects.filter(ceilphone=val1)
    if user:
        salts=user[0].salts
        h = hashlib.md5()
        password = salts + val2
        h.update(password.encode())
        if h.hexdigest()==user[0].password:
            return HttpResponse('1')

    return HttpResponse('0')

def login_redir(request):
    val1=request.GET.get('val1')
    # val2=request.GET.get('val2')
    print(val1)
    user=User.objects.filter(ceilphone=val1)[0]

    user_id=user.id
    request.session['user_id']=user_id
    user.user_status=1
    user.save()
    request.session['user_status']=user.user_status
    request.session['ceilphone']=val1

    car=request.session.get('car')
    if car:
        del request.session['car']
        return redirect('shop:paypage')
    return redirect('home:display:page')

def leave_out(request):

    del request.session['user_status']

    return redirect('home:display:page')

def check_email_page(request):
    #取出session中的注册的邮箱
    txt_username=request.session['txt_username']

    #生成随机的验证码


    #将生成的随机验证码存入session


    #转发模板
    return render(request,'admins_app/registerok.html')

def check_email_logic(request):
    #收取用户输入的验证码
    code=request.GET.get('')

    #从session中获取生成的随机验证码
    code2=request.session['']

    #检验两个用户输入的验证码是否正确
    if code.lower()==code2.lower():
        #正确则取出session中存取的注册信息
        email=request.session.get('email')
        nicname=request.session.get('nicname')
        password=request.session.get('password')

        #控制事务将注册信息存入数据库
        try:
            with transaction.atomic():
                #将注册信息存入数据库
                pass
        except:
            print('error')
            traceback.print_exc()
            #跳转到注册页面
            return

    #在cookie中存入一个标记，以便在错误跳转是给出提示

    #跳转邮箱验证页面
    return


def user_phone_blur(request):
    val=request.GET.get('val')
    rule=re.compile('@')

    if rule.findall(val):
        rule1 = re.compile('\w{3,9}@\w{2,3}\.\w{2,3}')
        if User.objects.filter(email=val):
            return HttpResponse('2')

        elif rule1.findall(val):
            return HttpResponse('1')
        return HttpResponse('0')
    if User.objects.filter(ceilphone=val):
        return HttpResponse('2')
    if len(val)!=11:
        return HttpResponse('0')
    if val.isdigit():
        return HttpResponse('1')
    else:
        return HttpResponse('0')

def numchar(n):
    a,b,c=0,0,0
    for i in n:
        if i.isdigit():
            a=1
        elif i.isalpha():
            b=1
        else:
            c=1
    num=a+b+c
    return num


def register_pwd_blur(request):
    val=request.GET.get('val')
    if 6<=len(val):
        return HttpResponse('1')
        # num=numchar(val)
        # if num==1:
        #     return HttpResponse('1')
        # elif num==2:
        #     return HttpResponse('2')
        # else:
        #     return HttpResponse('3')
    return HttpResponse('0')



def register_pwd_keyup(request):
    val=request.GET.get('val')

    if len(val)>=6:

        num=numchar(val)

        if num==1:
            return HttpResponse('1')
        elif num==2:
            return HttpResponse('2')
        else:
            return HttpResponse('3')
    return HttpResponse('0')


def repassword_blur(request):
    val1=request.GET.get('val1')
    val2=request.GET.get('val2')

    if val1==val2:
        return HttpResponse('1')
    return HttpResponse('0')


def getCaptcha(request):
    image=ImageCaptcha(fonts=[os.path.abspath('font/segoesc.ttf')])
    code_list=random.sample(string.ascii_uppercase+string.ascii_lowercase+string.digits,4)
    code="".join(code_list)
    request.session['code']=code
    print(code)
    data=image.generate(code)
    return HttpResponse(data,'image/png')

def resureCaptcha(request):
    val=request.GET.get('val')
    code=request.session.get('code')
    if len(val)==len(code):
        if val.lower()==code.lower():
            return HttpResponse('1')
        return HttpResponse('0')
    return HttpResponse('2')


def capt_keyup(request):
    code=request.session.get('code')
    val=request.GET.get('val')
    if len(val)<4:
        return HttpResponse('0')

    if code.lower()==val.lower():
        return HttpResponse('1')
    return HttpResponse('2')


