from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('register/',include(([path('page/',views.register_page,name='page'),
    						   path('logic/',views.register_logic,name='logic'),
                               path('phoneblur/',views.user_phone_blur,name='phoneblur'),
                               path('pwdblur/',views.register_pwd_blur,name='pwdblur'),
                               path('pwdkeyup/',views.register_pwd_keyup,name='pwdkeyup'),
                               path('repassword/',views.repassword_blur,name='repassword'),
                               path('getCaptcha/',views.getCaptcha,name='getCaptcha'),
                               path('resurecapt/',views.resureCaptcha,name='resurecapt'),
                               path('captkeyup/',views.capt_keyup,name='captkeyup'),
                               path('ok/',views.register_ok,name='ok')],'register'))),

    path('login/',include(([path('page/',views.login_page,name='page'),
                            path('logic/',views.login_logic,name='logic'),
                            path('redirct',views.login_redir,name='redirect'),
                            path('leaveout/',views.leave_out,name='out')],'login')))

]