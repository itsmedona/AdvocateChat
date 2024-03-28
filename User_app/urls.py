
from django.urls import path
from . import views

urlpatterns = [
    path('userregister',views.userregister, name='userregister'),
    path('usrlogin',views.usrlogin, name='usrlogin'),
    path('userregisfn',views.userregisfn, name='userregisfn'),
    path('userlogin',views.userlogin, name='userlogin'),
    path('userdashboard/',views.userdashboard, name='userdashboard'),
    path('userviewprofile',views.userviewprofile, name='userviewprofile'),
    path('usereditprofile/<int:id>/',views.usereditprofile,name='usereditprofile'),
    path('userdelete/<int:id>/',views.userdelete,name='userdelete'),
    path('userupdate/<int:id>/',views.userupdate,name='userupdate'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('law/<str:law>/',views.law,name='law'),
    path('bookadv/<int:id>/',views.bookadv,name='bookadv'),
    path('useradvprofile/<int:id>/',views.useradvprofile,name='useradvprofile'),
    path('bookcase',views.bookcase,name='bookcase'),
    path('userviewcase/',views.userviewcase, name='userviewcase'),
    path('resubmit/<int:id>/',views.resubmit,name='resubmit'),
    path('casestatus',views.casestatus,name='casestatus'),
    path('userviewipc',views.userviewipc, name='userviewipc'),
    path('resubmitcasedetails/<int:id>/',views.resubmitcasedetails, name='resubmitcasedetails')
]







