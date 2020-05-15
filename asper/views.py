from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.


def Index(request):
    return render(request, 'index.html')

def Login2(request):
    return render(request, 'login.html')

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
        elif 'projectname' in request.POST:

            Projectname = request.POST['projectname']
            Profiletitle = request.POST['projecttype']
            projectimg = request.FILES['projectimg']
            Project.objects.create(usr=request.user, ProjectName=Projectname, ProjectType=Profiletitle, ProjectImg=projectimg)
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
        phone = dd['Phone']
        i = request.FILES['img']
        udata = User.objects.filter(username=u)
        if udata:
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

def Work(request):
    userdata = UserDetail.objects.filter(usr=request.user).first()
    pdata = Project.objects.all()

    return render(request, 'work.html',{'userdata': userdata, 'project':pdata})

def Yourtask(request):
    userdata = UserDetail.objects.filter(usr=request.user).first()

    if userdata.dept == 'Design':

        assi = DesignAssignment.objects.all()
        design = DesignSubmit.objects.all()

    elif userdata.dept == 'Web':

        assi = WebAssignment.objects.all()
        design = WebSubmit.objects.all()
    elif userdata.dept == 'App':

        assi = AppAssignment.objects.all()
        design = AppSubmit.objects.all()
    else:
        return redirect('Profile')

    if request.method == "POST":
        if 'designimg' in request.FILES:

            i = request.FILES['designimg']
            n = request.POST['number']
            print(n)
            if userdata.dept == 'Design':
                DesignSubmit.objects.create(usr=request.user, AssignNo=n, Assignmentimng=i)
                return redirect('Yourtask')

            elif userdata.dept == 'Web':
                WebSubmit.objects.create(usr=request.user, Assignmentimng=i)
                return redirect('Yourtask')
            elif userdata.dept == 'App':
                AppSubmit.objects.create(usr=request.user, Assignmentimng=i)
                return redirect('Yourtask')

        elif 'check' in request.POST:
            if userdata.dept == 'Design':
                DesignSubmit.objects.update(usr=request.user, Status='True')
                return redirect('Yourtask')
            elif userdata.dept == 'Web':
                WebSubmit.objects.update(usr=request.user, Status='True')
                return redirect('Yourtask')
            elif userdata.dept == 'App':
                AppSubmit.objects.update(usr=request.user, Status='True')
                return redirect('Yourtask')



    return render(request, 'youtask.html',{'userdata':userdata, 'assi':assi, 'design':design})