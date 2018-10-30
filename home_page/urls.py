from django.urls import path, include

from . import views

urlpatterns=[
    path('display/',include(([path('page/',views.display_page,name='page'),
                              path('booklist/',views.book_list,name='booklist')],
                             'display'))),
    path('detail/',views.book_details,name='detail'),


]