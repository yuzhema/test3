from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from home_page.models import FirstCategory, SecondCategory, Books


def display_page(request):
    first=FirstCategory.objects.all()
    second=SecondCategory.objects.all()
    books1=Books.objects.all().order_by('-publish_time')[0:8]
    books2=Books.objects.filter(editor_recommend=True)[0:10]
    books3=Books.objects.filter(publish_time__gte='2018-10-10').order_by('sales')[0:7]
    books4=Books.objects.all().order_by('stock')[:10]
    return render(request,'home_page/index.html',{'first':first,'second':second,'books1':books1,'books2':books2,'books3':books3,'books4':books4})


def book_list(request):
    fid=request.GET.get('fid')
    sid=request.GET.get('sid')
    first = FirstCategory.objects.get(pk=fid)
    second = first.secondcategory_set.all()
    num=request.GET.get('num')
    inp = request.GET.get('inp')
    d=request.GET.get('d')

    cursor=request.GET.get('cursor')
    if not cursor:
        cursor=0

    sec=None
    if sid:
        print(sid)
        sec=SecondCategory.objects.get(pk=sid)

        if d=='销量':
            books=sec.books_set.all().order_by('sales')
        elif d=='价格':
            books = sec.books_set.all().order_by('dang_price')
        elif d=='出版时间':
            books = sec.books_set.all().order_by('publish_time')
        else:
            books=sec.books_set.all()

        if cursor=='1':
            books = sec.books_set.all().order_by('dang_price')
        elif cursor=='2':
            books = sec.books_set.all().order_by('sales')
        elif cursor=='3':
            books = sec.books_set.all().order_by('-dang_price')
        elif cursor == '4':
            books = sec.books_set.all().order_by('-sales')

    else:
        l=[]

        for i in second:
            l.append(i.id)
        if d=='销量':
            books=Books.objects.filter(second_id__in=l).order_by('sales')
        elif d=='价格':
            books = Books.objects.filter(second_id__in=l).order_by('dang_price')
        elif d=='出版时间':
            books = Books.objects.filter(second_id__in=l).order_by('publish_time')
        else:
            books=Books.objects.filter(second_id__in=l)

        if cursor=='1':
            books = Books.objects.filter(second_id__in=l).order_by('dang_price')
        elif cursor=='2':
            books = Books.objects.filter(second_id__in=l).order_by('sales')
        elif cursor=='3':
            books = Books.objects.filter(second_id__in=l).order_by('-dang_price')
        elif cursor == '4':
            books = Books.objects.filter(second_id__in=l).order_by('-sales')

    if not num:
        num=1
    if inp:
        num=inp

    pa=Paginator(object_list=books,per_page=1)
    p1=pa.page(1)
    c=p1.paginator.num_pages
    if int(num)>c:
        num=1
    page=pa.page(num)
    return render(request,'home_page/booklist.html',{'page': page,'first':first,'second':second,'sec':sec,'books':books,'d':d,'cursor':cursor})


def book_details(request):

    id=request.GET.get('id')
    book=Books.objects.get(pk=id)

    return render(request,'home_page/Bookdetails.html',{'book':book})



