from turtle import update
from django.shortcuts import render, redirect
from Advocate_app.models import Advocatedb
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse, JsonResponse

from User_app.models import BookAdvocatedb, Userdb

# Create your views here.
def homeindex(request):
    data = Advocatedb.objects.all()
    return render(request,'homeindex.html',{'data':data})

def userindex(request):
    data = Advocatedb.objects.all()
    return render(request,'userindex.html',{'data':data})

def view(request):
    return render(request,'view.html')

def advocateindex(request):
    return render(request,'advocateindex.html')

def advocateregister(request):
    return render(request,'advocateregister.html')
def adminhome(request):
    return render(request,'adminhome.html')
def advocatelogin(request):
    return render(request,'advocatelogin.html')

def advocatedashboard(request):
    return render(request,'advocatedashboard.html')

def advocateregisfn(request):
    if request.method == 'POST':
        adname = request.POST.get('adname')
        mobilenumber =request.POST.get('mobilenumber')
        emailid = request.POST.get('emailid')
        advocatetype = request.POST.get('advocatetype')
        district = request.POST.get('district')
        image = request.FILES['image']
        username = request.POST.get('username')
        password = request.POST.get('password')

        data = Advocatedb(adname=adname,mobilenumber=mobilenumber,emailid=emailid,advocatetype=advocatetype,district=district,image=image,username=username,password=password)
        data.save()
        return render(request,'Advocateindex.html')
    

def advlogin(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        if Advocatedb.objects.filter(username=username,password=password,status=1).exists():
            data = Advocatedb.objects.filter(username=username,password=password).values('id','adname','mobilenumber','emailid','advocatetype','district','image').first()
            request.session['username'] = username
            request.session['password'] = password
            request.session['advid'] = data['id']
            request.session['adname']= data['adname']
            advocate_id = request.session.get('advid')
            print(advocate_id)
            return redirect('advocatedashboard')
        else:
            messages.info(request,'Invalid user credentials')
            return redirect("advocatelogin")
    else:
        return redirect("advocatelogin")


def advviewprofile(request):
    advocate_id = request.session.get('advid')
    data = Advocatedb.objects.filter(id=advocate_id)
    return render(request,'advviewprofile.html',{'data':data})

def adveditprofile(request,id):
    data = Advocatedb.objects.filter(id=id)
    return render(request,'adveditprofile.html',{'data':data})

def advdelete(request,id):
    Advocatedb.objects.filter(id=id).delete()
    return redirect('advviewprofile')

def advupdate(request, id):
    if request.method == "POST":
        adname = request.POST.get('adname') 
        mobilenumber = request.POST.get('mobilenumber')
        emailid = request.POST.get('emailid')
        advocatetype = request.POST.get('advocatetype')
        district = request.POST.get('district')
        try:
            image = request.FILES['image']
            aa = FileSystemStorage()
            file = aa.save(image.name,image)

        except MultiValueDictKeyError:
            file=Advocatedb.objects.get(id=id.image)
            username = request.POST.get('username')
            password = request.POST.get('password')
       
            Advocatedb.objects.filter(id=id).update(adname=adname,mobilenumber=mobilenumber,emailid=emailid,advocatetype=advocatetype,district=district,username=username,password=password,image=file)
            return redirect('advocatedashboard')

def advlogout(request):
    del request.session['username']
    del request.session['password']
    del request.session['advid']
    del request.session['adname']
    return render(request,'homeindex.html')

def advviewcase(request):
    advocateid = request.session.get('advid')
    print(advocateid)
    data = BookAdvocatedb.objects.filter(advocateid=advocateid, status=0)
    
    print(data)
    return render (request,'advviewcase.html',{'data':data})


def allocateRoom(request, id):
    data = BookAdvocatedb.objects.filter(id=id)
    print(data)
    return render(request,'allocateRoom.html',{'data':data})

def submitroom(request, id):
    if request.method == 'POST':
        Room = request.POST.get('Room')
        print(update)
        BookAdvocatedb.objects.filter(id=id).update(Room=Room, status=1, update="Case Accepted")
        return redirect('advocatedashboard')
    else :
        return redirect('advocatedashboard')

def rejectcas(request, id):
    data = BookAdvocatedb.objects.filter(id=id)
    print(data)
    return render(request,'rejectcase.html',{'data':data})

def rjcase(request, id):
    if request.method == 'POST':
        update = request.POST.get('update')
        print(update)
        BookAdvocatedb.objects.filter(id=id).update(update=update, status=2)
        return redirect('advocatedashboard')
    else :
        return redirect('advocatedashboard')


        
def viewrejectedcase(request):
    advocateid = request.session.get('advid')
    print(advocateid)
    data = BookAdvocatedb.objects.filter(advocateid=advocateid, status=2)
    
    print(data)
    return render (request,'viewrejectedcase.html',{'data':data})

def deletecase(request, id):
    BookAdvocatedb.objects.filter(id=id).delete()
    return redirect('advocatedashboard')

def recase(request):
    advocateid = request.session.get('advid')
    print(advocateid)
    data = BookAdvocatedb.objects.filter(advocateid=advocateid, status=3)
    
    print(data)
    return render (request,'viewrejectedcase.html',{'data':data})

def acptcase(request):
    advocateid = request.session.get('advid')
    print(advocateid)
    data = BookAdvocatedb.objects.filter(advocateid=advocateid, status=1)
    
    print(data)
    return render (request,'acceptedcase.html',{'data':data})


def closecase(request, id):
    data = BookAdvocatedb.objects.filter(id=id).update(update="Case Closed", status=4)
    print(data)
    return render(request,'advocatedashboard.html')



# def advchat(request):
#     return render(request, 'advchhome.html')