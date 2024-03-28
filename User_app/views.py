from django.shortcuts import render, redirect
from Admin_app.models import IPCSections, Lawsdb,Law
from User_app.models import BookAdvocatedb, Userdb
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from Advocate_app.models import *

# Create your views here.
def userregister(request):
    return render(request,'userregister.html')

def userdashboard(request):
    da = Law.objects.all()
    return render(request, 'userdashboard.html',{'lawtype':da})

def userlogin(request):
    return render(request,'userlogin.html')


def userregisfn(request):
    if request.method == 'POST':
        usrname = request.POST.get('usrname')
        mobilenumber =request.POST.get('mobilenumber')
        emailid = request.POST.get('emailid')
        district = request.POST.get('district')
        image = request.FILES['image']
        username = request.POST.get('username')
        password = request.POST.get('password')

        data = Userdb(usrname=usrname,mobilenumber=mobilenumber,emailid=emailid,district=district,image=image,username=username,password=password)
        data.save()
        return render(request,'userindex.html')


def usrlogin(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        if Userdb.objects.filter(username=username,password=password,status=1).exists():
            data = Userdb.objects.filter(username=username,password=password).values('id','usrname','mobilenumber','emailid','district','image').first()
            request.session['username'] = username
            request.session['password'] = password

            request.session['mobilenumber'] = data['mobilenumber']
            request.session['district'] = data['district']

            request.session['usrid'] = data['id']
            request.session['usrname']= data['usrname']
            user_id = request.session.get('usrid')
            print(user_id)
            return render(request,'userdashboard.html')
        else:
            messages.info(request,'Invalid user credentials')
            return redirect("userlogin")
    else:
        return redirect("userlogin")

def userviewprofile(request):
    user_id = request.session.get('usrid')
    data = Userdb.objects.filter(id=user_id)
    return render(request,'userviewprofile.html',{'data':data})


def usereditprofile(request,id):
    data = Userdb.objects.filter(id=id)
    return render(request,'usereditprofile.html',{'data':data})

def userdelete(request,id):
    Userdb.objects.filter(id=id).delete()
    return redirect('userviewprofile')

def userupdate(request, id):
    if request.method == "POST":
        usrname = request.POST.get('usrname') 
        mobilenumber = request.POST.get('mobilenumber')
        emailid = request.POST.get('emailid')
        district = request.POST.get('district')
        try:
            image = request.FILES['image']
            aa = FileSystemStorage()
            file = aa.save(image.name,image)

        except MultiValueDictKeyError:
            file=Userdb.objects.get(id=id.image)
            username = request.POST.get('username')
            password = request.POST.get('password')
       
            Userdb.objects.filter(id=id).update(usrname=usrname,mobilenumber=mobilenumber,emailid=emailid,district=district,username=username,password=password,image=file)
            return redirect('userdashboard')

def userlogout(request):
    del request.session['username']
    del request.session['password']
    del request.session['usrid']
    del request.session['usrname']
    return render(request,'homeindex.html')

def law(request,law):
    data = Advocatedb.objects.filter(advocatetype=law,status=1)
    print(data)
    return render(request,'law.html',{'data':data})

def useradvprofile(request,id):
    data = Advocatedb.objects.filter(id=id)
    return render(request,'useradvprofile.html',{'data':data})

def bookadv(request, id):
    data = Advocatedb.objects.filter(id=id)
    print(data)
    # value = "{{request.session.usrname}}"
    userid = request.session.get('usrid')
    return render(request,'bookadvocate.html',{'data':data})


def bookcase(request):
    if request.method == 'POST':

        query = request.POST.get('query')
        image = request.FILES['image']
        userid = request.session.get('usrid')
        advocateid = request.POST.get('advocateid')
        data = BookAdvocatedb(userid=Userdb.objects.get(id=userid),advocateid=Advocatedb.objects.get(id=advocateid),query=query,image=image)
        data.save()
        return render(request,'userdashboard.html')

def userviewcase(request):
    advocateid = request.session.get('advid')
    print(advocateid)
    data = BookAdvocatedb.objects.filter(advocateid=advocateid, status__in=[0,1]) 
    print(data)
    return render (request,'userviewcase.html',{'data':data})


def resubmit(request, id):
    print(id)
    data = BookAdvocatedb.objects.filter(id=id)
    print(data)
    return render(request,'resubmitcase.html',{'data':data})

    
def resubmitcasedetails(request, id):
    if request.method == "POST":
        query = request.POST.get('query') 
        userid = request.session.get('usrid')
        advocateid = request.POST.get('advocateid')
       
        try:
            image = request.FILES['image']
            aa = FileSystemStorage()
            file = aa.save(image.name,image)

        except MultiValueDictKeyError:
            file=Userdb.objects.get(id=id.image)
            
        BookAdvocatedb.objects.filter(id=id).update(query=query,userid=Userdb.objects.get(id=userid),advocateid=Advocatedb.objects.get(id=advocateid),image=file,status=3,update="Not Viewed By Advocate")
        return redirect('userdashboard')

def casestatus(request):
    userid = request.session.get('usrid')
    print("Session = ",userid)
    data = BookAdvocatedb.objects.filter(userid=userid, status__in=[2,3,1]) 
    print(data)
    return render (request,'viewcasestatus.html',{'data':data})

def userviewipc(request):
    data = IPCSections.objects.all()
    print(data)
    return render (request,'userviewipc.html',{'data':data})
    

