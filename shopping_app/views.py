import random
import string
import traceback

from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from admins_app.models import User
from home_page.models import Books
from shopping_app.cart import Cart
from shopping_app.cart2 import Cart2
from shopping_app.models import Address, Order, UserOrder


def add_cart(request):
    book_id = request.GET.get('book_id')
    num=request.GET.get('val')
    aa=request.GET.get('aa')

    if not num:
        num=1

    cart = request.session.get('cart')
    if not cart:
        cart = Cart()

    cart.add(int(book_id),int(num))
    request.session['cart'] = cart

    if aa:
        print('delete .........')
        cart2=request.session.get('cart2')
        cart2.delete(int(book_id))
        request.session['cart2']=cart2

    return HttpResponse('1')

def showCart(request):
    cart=request.session.get('cart')
    if cart:
        return HttpResponse('1')

def modify_cart(request):
    print(11111111111)
    book_id=request.GET.get('book_id')
    amount=request.GET.get('val')
    cart=request.session['cart']
    cart.modify(book_id,int(amount))
    request.session['cart']=cart

    return HttpResponse('1')

def delete_cart(request):
    book_id=request.GET.get('book_id')
    cart=request.session.get('cart')

    cart.delete(int(book_id))
    request.session['cart']=cart
    total_price=cart.total_price
    return JsonResponse({'total_price':total_price})



def shopping_car(request):

    address=Address.objects.all()

    return render(request,'shopping_app/car.html',{"address":address})


def get_book(request):

    book_id=request.GET.get('book_id')
    amounts=request.GET.get('amounts')
    cart=request.session.get('cart')
    for i in cart.catalogue:
        if i.book.id==int(book_id):
            i.amount=int(amounts)
            price=i.amount*i.book.dang_price
            cart.sum()
            total_price=cart.total_price
            per_price=i.book.dang_price

    request.session['cart']=cart

    return JsonResponse({'price':price,'total_price':total_price,'per_price':per_price})


def check_all(request):

    cart=request.session.get('cart')
    total_price=cart.total_price
    save_price=cart.save_price
    return JsonResponse({"total_price":total_price,'save_price':save_price})

def delMany(request):
    s=request.GET.get('s')
    cart=request.session.get('cart')
    l=s.split(',')
    for i in l:
        if i:
            cart.delete(int(i))
    request.session['cart']=cart

    return HttpResponse('1')



def pay(request):

    #从购物车页面获取地址信息
    option=request.GET.get('option')
    request.session['option']=option

    #从购物车页面获取的订单总价格
    total_price=request.GET.get('total_price')
    request.session['total_price'] = total_price

    #从购物车中取出所购买的商品数量
    commodity_count = request.GET.get('commodity_count')
    request.session['commodity_count'] = commodity_count

    #从购物车页面获取的所选的id字符串
    s=request.GET.get('s')
    request.session['s'] = s

    # 从购物车页面获取的所选的书籍数量字符串
    count=request.GET.get('count')
    request.session['count'] = count

    #从购物车页面取出单个商品的总价字符串
    one_total_price=request.GET.get('one_total_price')
    request.session['one_total_price']=one_total_price


    # 将s字符串分解为单个字符存到l_ids列表中
    book_ids = s.split(',')

    # 从session中取出所买书的数量字符串
    counts = request.session.get('count')
    # 将counts字符串分解为单个字符存到l_counts列表中
    order_counts = counts.split(',')

    # 恢复购物车
    cart2 = Cart2()
    for i in range(len(book_ids) - 1):
        cart2.add(int(book_ids[i]), int(order_counts[i]))
    request.session['cart2'] = cart2

    cart = request.session.get('cart')
    book_ids = request.session.get('s').split(',')

    # 从购物车中删除图书
    for i in range(len(book_ids) - 1):
        cart.delete(int(book_ids[i]))
    request.session['cart'] = cart



    #购物车标记
    car=request.GET.get('car')
    user_status=request.session.get('user_status')
    if user_status:
        return redirect('shop:paypage')
    request.session['car']=car
    return redirect('user:login:page')

def pay_page(request):
    option=request.session.get('option')

    if option =='0':
        return render(request,'shopping_app/indent.html')
    address=Address.objects.get(pk=option)

    return render(request, 'shopping_app/indent.html',{'address':address})


def order(request):
    #收参
    name=request.POST.get('name')
    address=request.POST.get('address')
    zip=request.POST.get('zip')
    ceilphone=request.POST.get('ceilphone')
    telphone=request.POST.get('telphone')
    user_id=request.session.get('user_id')



    # 从session中取出订单的总价格
    total_price = request.session.get('total_price')  # //总价

    #从session中取出所购买的书的id字符串
    ids=request.session.get('s')
    # 将id字符串分解为单个字符存到l_ids列表中
    book_ids = ids.split(',')

    #从session中取出所买书的数量字符串
    '''订单数量'''
    counts=request.session.get('count')
    # 将counts字符串分解为单个字符存到l_counts列表中
    order_counts = counts.split(',')

    #从session中取出单个商品的总价字符串
    one_total_price=request.session.get('one_total_price')
    one_order_total_price=one_total_price.split(',')



    #创建随机订单号列表
    uuid=random.sample(string.digits,10)
    #将列表转成字符串
    order_uuid="".join(uuid)           #//订单号
    request.session['order_uuid']=order_uuid



    option=request.session.get('option')
    try:
        with transaction.atomic():
            '''地址存数据库'''
            c=User.objects.get(pk=user_id)    #//用户
            if option=='0':
                address=Address(name=name,detail_address=address,zipcode=zip,cellphone=ceilphone,telephone=telphone,users=c)
                address.save()                    #//地址
            else:
                address=Address.objects.get(pk=option)
            request.session['name']=address.name

            '''订单存数据库'''
            #订单
            order1=Order(total_price=total_price,order_uuid=order_uuid,user=c,address=address)
            order1.save()

            '''订单项存数据库'''

            for i in range(0,len(book_ids)-2):
                book=Books.objects.get(pk=book_ids[i])
                order_list=UserOrder(amount=int(order_counts[i]),total_price=int(one_order_total_price[i]),book=book,order=order1)
                order_list.save()

            return redirect('shop:success')

    except:
        print('error')
        traceback.print_exc()
        return redirect('shop:paypage')

def success_page(request):

    return render(request,'shopping_app/indent ok.html')


