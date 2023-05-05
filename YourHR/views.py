from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from YourHR.models import Apply
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_superuser:
        return redirect('/admin')
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')
    
def loginuser(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome User! Logged In')
            return redirect("/")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')
    
def logoutuser(request):
    logout(request)
    return redirect( '/login')

def aboutyou(request):
    f_name = request.user.first_name
    l_name = request.user.last_name
    user=request.user
    email=request.user.email
    apply = Apply.objects.filter(email=email)
    print(apply)
    context={
        'f_name':f_name,
        'l_name':l_name,
        'user':user,
        'email':email,
        'items':apply,
    }
    return render(request, 'aboutyou.html', context)

def createuser(request):
    if request.method=='POST':
        f_name=request.POST.get("f_name")
        l_name=request.POST.get("l_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user = User.objects.create_user(username, email, password)
        user.save()
        user.first_name=f_name
        user.last_name=l_name
        user.save()
        messages.success(request, 'Message Sent! We will contact you shortly')
        return redirect('/login')
    return render(request, 'register.html')

def jobs(request):
    if request.method=="POST":
        name = request.user.first_name
        email=request.user.email
        role=request.POST.get("role")
        why=request.POST.get("why")
        resume=request.POST.get("resume")
        apply=Apply(name=name, email=email, role=role, why=why, resume=resume, date=datetime.today())
        apply.save()
        messages.success(request, 'Job Applied! The recruiter Shal Contact you')
    return render(request, 'jobs.html')
