from django.urls import path, include

from . import views

urlpatterns=[
    path('main/',views.main,name='main'),
    path('add/',include(([path('page/',views.add_page,name='page'),
                          path('logic/',views.add_logic,name='logic')],'add'))),
    path('dzlist/',include(([path('page/',views.dzlist_page,name='page'),
                          path('del/',views.dzlist_del,name='del')],'dzlist'))),
    path('list/',include(([path('page/',views.list_page,name='page'),
                          path('del/',views.list_del,name='del')],'list'))),
    path('splb/',include(([path('page/',views.splb_page,name='page'),
                          path('add/',views.splb_add,name='add'),
                          path('del/',views.splb_del,name='del')],'splb'))),
    path('test/',include(([path('page/',views.test_page,name='page'),
                          path('logic/',views.test_logic,name='logic')],'test'))),
    path('zjsp/',include(([path('page/',views.zjsp_page,name='page'),
                          path('logic/',views.zjsp_logic,name='logic')],'zjsp'))),
    path('zjzlb/',include(([path('page/',views.zjzlb_page,name='page'),
                          path('logic/',views.zjzlb_logic,name='logic')],'zjzlb'))),

]