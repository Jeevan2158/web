from django.shortcuts import render,redirect
from .models import Destination
from urllib.request import Request
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

def home(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 70
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'First Biryani, Then Sherwani'
    dest2.img = 'destination_2.jpg'
    dest2.price = 65
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Bengaluru'
    dest3.desc = 'Beautiful City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 75
    dest3.offer = False

    dest4 = Destination()
    dest4.name = 'Mumbai'
    dest4.desc = 'The City That Never Sleeps'
    dest4.img = 'destination_4.jpg'
    dest4.price = 70
    dest4.offer = False

    dest5 = Destination()
    dest5.name = 'Hyderabad'
    dest5.desc = 'First Biryani, Then Sherwani'
    dest5.img = 'destination_5.jpg'
    dest5.price = 65
    dest5.offer = False


    dest6 = Destination()
    dest6.name = 'Bengaluru'
    dest6.desc = 'Beautiful City'
    dest6.img = 'destination_6.jpg'
    dest6.price = 75
    dest6.offer = True

    dests = [dest1, dest4, dest3, dest4, dest5, dest6]

    return render(request, "index.html", {'dests': dests})

def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if User.objects.filter(username=username):
            messages.error(request, 'username already taken')
            return redirect('signup') 
        if User.objects.filter(email=email):
            messages.error(request, 'email already taken')
            return redirect('signup')
        if pass1!=pass2:
            messages.error(request, 'password did not match')
            return redirect('signup')    
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your Account has been created")
        return redirect('signin')


    return render(request, 'signup.html')   

def signin(request):
    if request.method=="POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            messages.success(request,"login successfully",{'fname':fname})
            # return render(request, 'index.html',{'fname':fname})
            return redirect('home')
        else:
            messages.error(request, 'crediential not match') 
            return redirect('signin')   
            
    return render(request, 'signin.html')         

def signout(request):
    logout(request)
    messages.success(Request,"logout successfully")
    return render(request, 'signin.html')    