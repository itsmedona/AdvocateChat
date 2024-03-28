from django.urls import path
from . import views

urlpatterns = [
    path('Adminindex',views.Adminindex, name='Adminindex'),
    path('homeindex',views.homeindex, name='homeindex'),
    path('Addlaws',views.Addlaws, name='Addlaws'),
    path('Viewlaws',views.viewlaws, name='Viewlaws'),
    path('getlawdetails',views.getlawdetails, name='getlawdetails'),
    path('admincheck/',views.admincheck, name='admincheck'),
    path('adminlogin/',views.adminlogin, name='adminlogin'),
    path('Civillaw',views.Civillaw, name='Civillaw'),
    path('adminlogout',views.adminlogout, name='adminlogout'),
    path('adminviewcase',views.adminviewcase, name='adminviewcase'),
    path('addipcsections/',views.addipcsections, name='addipcsections'),
    path('addipcfn',views.addipcfn, name='addipcfn'),
    path('viewipcsections/',views.viewipcsections, name='viewipcsections'),
    path('approveadvocate/',views.approveadvocate, name='approveadvocate'),
    path('approveadv/<int:id>/',views.approveadv, name='approveadv'),
    path('deleteadv/<int:id>/',views.deleteadv,name='deleteadv'),
    path('approveuser/',views.approveuser, name='approveuser'),
    path('approveusr/<int:id>/',views.approveusr, name='approveusr'),
    path('deleteusr/<int:id>/',views.deleteusr,name='deleteusr')

]






