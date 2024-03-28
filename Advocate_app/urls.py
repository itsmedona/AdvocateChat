from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeindex, name='homeindex'),
    path('adminhome',views.adminhome, name='adminhome'),
    path('advocateindex',views.advocateindex, name='advocateindex'),
    path('advocatelogin',views.advocatelogin, name='advocatelogin'),
    path('advlogin',views.advlogin, name='advlogin'),
    path('advocateregister',views.advocateregister, name='advocateregister'),
    path('advocatedashboard',views.advocatedashboard, name='advocatedashboard'),
    path('advviewprofile',views.advviewprofile, name='advviewprofile'),
    path('adveditprofile/<int:id>/',views.adveditprofile,name='adveditprofile'),
    path('advdelete/<int:id>/',views.advdelete,name='advdelete'),
    path('advupdate/<int:id>/',views.advupdate,name='advupdate'),
    path('view/',views.view, name='view'),
    path('userindex',views.userindex, name='userindex'),
    path('advlogout',views.advlogout, name='advlogout'),
    path('advocateregisfn',views.advocateregisfn, name='advocateregisfn'),
    path('advlogout',views.advlogout, name='advlogout'),
    path('acceptcase/<int:id>/',views.adveditprofile,name='adveditprofile'),
    path('rejectcase/<int:id>/',views.advdelete,name='advdelete'),
    path('advviewcase',views.advviewcase, name='advviewcase'),
    path('allocateRoom/<int:id>/',views.allocateRoom, name='allocateRoom'),
    path('submitroom/<int:id>/',views.submitroom, name='submitroom'),
    path('rejectcas/<int:id>/',views.rejectcas, name='rejectcas'),
    path('rjcase/<int:id>/',views.rjcase, name='rjcase'),
    path('viewrejectedcase',views.viewrejectedcase, name='viewrejectedcase'),
    path('deletecase/<int:id>/',views.deletecase, name='deletecase'),
    path('closecase/<int:id>/',views.closecase, name='closecase'),
    path('recase',views.recase, name='recase'),
    path('acptcase',views.acptcase, name='acptcase'),
    
]








