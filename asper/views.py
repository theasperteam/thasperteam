from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from django.http import HttpResponse

# Create your views here.

def Test(request):
    return HttpResponse("<h1>test</h1>")

def Index(request):
    return render(request, 'index.html')

def Team(request):
    return render(request, 'team.html')

def Pillar(request):
    return render(request, 'founding.html')


def Profile(request):
    userdata = UserDetail.objects.filter(usr=request.user).first()
    first = FirstTask.objects.filter(usr=request.user).first()
    count = User.objects.count()
    if request.method == "POST":
        if 'img' in request.FILES:
            i = request.FILES['img']
            userdata.image = i
            userdata.save()
            return redirect('Profile')
        elif 'phone' in request.POST:
            phone = request.POST['phone']
            userdata.phone = phone
            userdata.save()
            return redirect('Profile')
        else:
            return redirect('Profile')

    return render(request, 'profile.html', {'userdata': userdata, 'first':first, 'count':count})

def SignIn(request):
    error = False
    if request.method == 'POST':
        x = request.POST
        us = x['usr']
        pa = x['pas']
        user = authenticate(username=us, password=pa)

        if user:
            login(request, user)
            return redirect('Profile')
        else:
            error = True
    d = {"error": error}
    return render(request, 'signin.html', d)

def SignUp(request):
    error = False
    if request.method == 'POST':
        dd = request.POST
        u = dd['username']
        fn = dd['Firstname']
        ln = dd['Lastname']
        e = dd['email']
        p = dd['password']
        p1 = dd['password1']
        phone = dd['Phone']
        i = request.FILES['img']
        udata = User.objects.filter(username=u)
        if udata:
            error = True
        elif p1 != p:
            error = True
        else:
            user = User.objects.create_user(username=u, password=p, email=e, first_name=fn, last_name=ln)
            UserDetail.objects.create(usr=user, image=i, phone=phone)
            return redirect('SignIn')
    d = {"error": error}
    return render(request, 'signup.html', d)

def Logout(request):
    logout(request)
    return redirect('SignIn')


def FirstTk(request):
    userdata = UserDetail.objects.filter(usr=request.user).first()
    if request.method == 'POST':
        d2 = request.POST
        q1 = d2['q1']
        q2 = d2['q2']
        q3 = d2['q3']
        q4 = d2['q4']
        q5 = d2['q5']
        q6 = d2['q6']
        q7 = d2['q7']
        q8 = d2['q8']
        FirstTask.objects.create(usr=request.user, Q1=q1, Q2=q2, Q3=q3, Q4=q4, Q5=q5, Q6=q6, Q7=q7, Q8=q8)
        return redirect('Profile')
    f = {userdata:'userdata'}
    return render(request, 'firsttask.html', f)

def AllProfile(request):
    adata= UserDetail.objects.filter(usr=request.user).first()
    udata = UserDetail.objects.all()
    return render(request, 'all_profile.html', {'udata':udata, 'adata':adata})