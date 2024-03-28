from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request, 'home.html')

def room(request, room):
    print("Hi Hi")
    username = request.GET.get('username') # henry
    room_details = Room.objects.all()
    return render(request, 'room.html', {

        'username': username,
        'room': room,
        'room_details': room_details,
    })

def checkview(request):
    room = request.POST['roomname']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def user_home(request):
    return render(request, 'user_home.html')

def user_checkview(request):
    print("Hello")
    user_room = request.POST['roomname']
    username = request.POST['username']

    if Room.objects.filter(name=user_room).exists():
        print("Username : ",username)
        return redirect('user_room',user_room,username)
    else:
        new_room = Room.objects.create(name=user_room)
        new_room.save()
        return redirect('/'+user_room+'/?username='+username)

def user_room(request,user_room,username):
    room_details = Room.objects.get(name=user_room)
    return render(request, 'user_room.html', {
        'username': username,
        'room': user_room,
        'room_details': room_details,
    })

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    # return HttpResponse("Hi, Message Sent Successfully!!")

def getMessages(request,  room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
