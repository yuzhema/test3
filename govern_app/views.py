from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from home_page.models import Books, SecondCategory, FirstCategory
from shopping_app.models import Address


def main(request):

    return render(request,'index.html')

def add_page(request):
    second=SecondCategory.objects.all()

    return render(request,'main/add.html',{'second':second})

def add_logic(request):
    name=request.POST.get('name')
    author=request.POST.get('author')
    print_house=request.POST.get('print_house')
    parent_id=request.POST.get('parent_id')
    date=request.POST.get('date')
    dang_price=request.POST.get('dang_price')
    price=request.POST.get('price')
    file=request.FILES.get('file')
    print(file)
    ids=request.session.get('id')
    print(ids)
    if ids:
        del request.session['id']
        parent_id=ids

    parent=SecondCategory.objects.get(pk=parent_id)
    print(name,author,print_house,parent_id,date,file)
    Books(bookname=name,author=author,book_publish=print_house,publish_time=date,second=parent,dang_price=dang_price,price=price,produce_image_path=file).save()

    return redirect('govern:add:page')

def dzlist_page(request):
    address=Address.objects.all()
    num=request.GET.get('num')
    if not num:
        num=1
    page=Paginator(object_list=address,per_page=10).page(int(num))
    return render(request,'main/dzlist.html',{"address":address,"page":page})


def dzlist_del(request):
    id=request.GET.get('id')
    Address.objects.get(pk=id).delete()
    print(id)
    return HttpResponse('1')


def list_page(request):
    books=Books.objects.all()

    l=[]
    for i in books:

        l.append({'id':i.id,'name':i.bookname,'author':i.author,'house':i.book_publish,'price':i.price,'dang_price':i.dang_price,'stock':i.stock})
    return render(request, 'main/list.html',{'books':books,'l':l})

def list_del(request):
    id=request.GET.get('id')
    Books.objects.get(pk=id).delete()
    print(id)
    return HttpResponse('1')


def splb_page(request):
    num=request.GET.get('num')
    num2=request.session.get('num')
    second=SecondCategory.objects.all()
    if not num:
        num=1

    if num2:
        del request.session['num']
        num=num2
    page=Paginator(object_list=second,per_page=20).page(int(num))

    return render(request, 'main/splb.html',{'page':page,'second':second})


def splb_add(request):
    id=request.GET.get('id')
    request.session['id']=id

    return redirect('govern:add:page')

def splb_del(request):
    num=request.GET.get('num')
    print(num,'************')
    id=request.GET.get('id')
    second=SecondCategory.objects.get(pk=id)
    second.delete()
    page=Paginator(object_list=SecondCategory.objects.all(),per_page=20).page(1)
    if page.paginator.num_pages<int(num) and int(num)>1:
        num=page.paginator.num_pages
    print(num, '************')
    request.session['num']=num
    return redirect('govern:splb:page')

def test_page(request):

    return render(request, 'main/test.html')


def test_logic(request):


    return render


def zjsp_page(request):

    return render(request, 'main/zjsp.html')


def zjsp_logic(request):

    val=request.GET.get('val')
    FirstCategory(parent_category=val).save()

    return HttpResponse('1')


def zjzlb_page(request):
    first=FirstCategory.objects.all()
    return render(request, 'main/zjzlb.html',{'first':first})


def zjzlb_logic(request):
    child_name=request.GET.get('child_name')
    father_id=request.GET.get('father_id')

    father=FirstCategory.objects.get(pk=father_id)
    SecondCategory(child_category=child_name,first=father).save()
    return HttpResponse('1')

