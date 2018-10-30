from django.urls import path

from . import views

urlpatterns=[

    path('cart/',views.shopping_car,name='cart'),
    path('add/',views.add_cart,name='add'),
    path('modify/',views.get_book,name='modify'),
    path('delete/',views.delete_cart,name='delete'),
    path('checkall/',views.check_all,name='checkall'),
    path('delmany/',views.delMany,name='delmany'),
    path('pay/',views.pay,name='pay'),
    path('pay/page/',views.pay_page,name='paypage'),
    path('order/',views.order,name='order'),
    path('success/page/',views.success_page,name='success')

]