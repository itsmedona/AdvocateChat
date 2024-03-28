from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from Admin_app.models import IPCSections, Law, Lawsdb
from Advocate_app.models import Advocatedb
from User_app.models import BookAdvocatedb, Userdb

# Create your views here.
def Adminindex(request):
    count = Advocatedb.objects.filter(status=0).count()
    print(count)
    countaccptcase = BookAdvocatedb.objects.filter(status__in=[0,1,2,3,4]).count()
    countuser = Userdb.objects.filter(status=0).count()
    countnoti = count+countaccptcase+countuser
    accepted_users = Userdb.objects.filter(status=1).count()
    accepted_advocates = Advocatedb.objects.filter(status=1).count()
    accepted_case = BookAdvocatedb.objects.filter(status=1).count()
    return render(request,'Adminindex.html',{'count':count, 'countuser':countuser, 'countaccptcase':countaccptcase, 'countnoti':countnoti,'accepted_users':accepted_users,'accepted_advocates':accepted_advocates,'accepted_case':accepted_case})
    
def homeindex(request,law):
    return render(request,'homeindex.html')
    
def adminlogin(request):
    return render(request,'adminlogin.html')   

def Addlaws(request):
    count = Advocatedb.objects.filter(status=0).count()
    print(count)
    countaccptcase = BookAdvocatedb.objects.filter(status__in=[0,1,2,3,4]).count()
    countuser = Userdb.objects.filter(status=0).count()
    countnoti = count+countaccptcase+countuser
    return render(request,'Addlaws.html',{'count':count, 'countuser':countuser, 'countaccptcase':countaccptcase, 'countnoti':countnoti})

def Viewlaws(request):
    count = Advocatedb.objects.filter(status=0).count()
    print(count)
    countaccptcase = BookAdvocatedb.objects.filter(status__in=[0,1,2,3,4]).count()
    countuser = Userdb.objects.filter(status=0).count()
    countnoti = count+countaccptcase+countuser
    return render(request,'Viewlaws.html',{'count':count, 'countuser':countuser, 'countaccptcase':countaccptcase, 'countnoti':countnoti})

def getlawdetails(request):
    if request.method == 'POST':
        count = Advocatedb.objects.filter(status=0).count()
        print(count)
        countaccptcase = BookAdvocatedb.objects.filter(status__in=[0,1,2,3,4]).count()
        countuser = Userdb.objects.filter(status=0).count()
        countnoti = count+countaccptcase+countuser
        lawtype = request.POST.get('lawtype')
        lawname = request.POST.get('lawname')
        lawdescription = request.POST.get('lawdescription')
        data = Lawsdb(lawtype=lawtype,lawname=lawname,lawdescription=lawdescription)
        data.save()
        return redirect('Addlaws',{'count':count, 'countuser':countuser, 'countaccptcase':countaccptcase, 'countnoti':countnoti})

def viewlaws(request):
    data = Lawsdb.objects.all()
    print(data)
    count = Advocatedb.objects.filter(status=0).count()
    print(count)
    countaccptcase = BookAdvocatedb.objects.filter(status__in=[0,1,2,3,4]).count()
    countuser = Userdb.objects.filter(status=0).count()
    countnoti = count+countaccptcase+countuser
    return render (request,'viewlaws.html',{'data':data,'count':count, 'countuser':countuser, 'countaccptcase':countaccptcase, 'countnoti':countnoti}) 

def admincheck(request):
    username_r = request.POST.get('username')
    password_r = request.POST.get('password')
    print(username_r)
    print(password_r)
    if User.objects.filter(username__contains=username_r).exists():
        user = authenticate(username=username_r,password=password_r)
        if user is not None:
            login(request,user)
            return redirect('Adminindex') 
        else:
            return render(request,'adminlogin.html',{'msg':'Invalid user credentials'})
    else:
        return render(request,'adminlogin.html',{'msg':'Invalid user credentials'}) 

def adminlogout(request):
    return render(request,'homeindex.html')

def Civillaw(request):
    return render(request,'Civillaw.html')

def approveadvocate(request):
    count = Advocatedb.objects.filter(status=0).count()
    print(count)
    countaccptcase = BookAdvocatedb.objects.filter(status__in=[0,1,2,3,4]).count()
    countuser = Userdb.objects.filter(status=0).count()
    countnoti = count+countaccptcase+countuser
    data = Advocatedb.objects.filter(status=0)
    return render(request,'approveadvocate.html',{'data':data,'count':count, 'countuser':countuser, 'countaccptcase':countaccptcase, 'countnoti':countnoti})

def approveadv(request, id):
        Advocatedb.objects.filter(id=id).update(status=1)
        return redirect('approveadvocate')

def deleteadv(request, id):
    Advocatedb.objects.filter(id=id).delete()
    return redirect('approveadvocate')
    
def approveuser(request):
    data = Userdb.objects.filter(status=0)
    countaccptcase = BookAdvocatedb.objects.filter(status__in=[0,1,2,3,4]).count()
    count = Advocatedb.objects.filter(status=0).count()
    print(count)
    countuser = Userdb.objects.filter(status=0).count()
    countnoti = count+countaccptcase+countuser
    return render(request,'approveuser.html',{'data':data,'count':count, 'countuser':countuser, 'countaccptcase':countaccptcase, 'countnoti':countnoti})

def approveusr(request, id):
    Userdb.objects.filter(id=id).update(status=1)
    return redirect('approveuser')

def deleteusr(request, id):
    Userdb.objects.filter(id=id).delete()
    return redirect('approveuser')

def adminviewcase(request):
    advocateid = request.session.get('advid')
    print(advocateid)
    countaccptcase = BookAdvocatedb.objects.filter(status__in=[0,1,2,3,4]).count()
    count = Advocatedb.objects.filter(status=0).count()
    countuser = Userdb.objects.filter(status=0).count()
    countnoti = count+countaccptcase+countuser
    data = BookAdvocatedb.objects.filter(advocateid=advocateid, status__in=[0,1,2,3,4]) 
    print(data)
    return render (request,'adminviewcase.html',{'data':data, 'countaccptcase':countaccptcase ,'count':count, 'countuser':countuser, 'countnoti':countnoti})


def addipcsections(request):
    count = Advocatedb.objects.filter(status=0).count()
    print(count)
    countaccptcase = BookAdvocatedb.objects.filter(status__in=[0,1,2,3,4]).count()
    countuser = Userdb.objects.filter(status=0).count()
    countnoti = count+countaccptcase+countuser
    da = Law.objects.all()
    print(da)
    return render(request,'addipcsections.html',{'count':count, 'countuser':countuser, 'countaccptcase':countaccptcase, 'countnoti':countnoti, 'lawtype':da})

def addipcfn(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        ipcsection = request.POST.get('ipcsection')
        ipcdescription = request.POST.get('ipcdescription')
        data = IPCSections(type=Law.objects.get(id=type),ipcsection=ipcsection,ipcdescription=ipcdescription)
        data.save()
        return redirect('addipcsections')

def viewipcsections(request):
    data = IPCSections.objects.all()
    print(data)
    count = Advocatedb.objects.filter(status=0).count()
    print(count)
    countaccptcase = BookAdvocatedb.objects.filter(status__in=[0,1,2,3,4]).count()
    countuser = Userdb.objects.filter(status=0).count()
    countnoti = count+countaccptcase+countuser
    return render (request,'viewipcsections.html',{'data':data,'count':count, 'countuser':countuser, 'countaccptcase':countaccptcase, 'countnoti':countnoti})
    
