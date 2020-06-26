from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from datetime import date,datetime

# Create your views here.
# temp files


#main files

def Index(request):
    return render(request, 'index2.html')



def Team(request):
    return render(request, 'team.html')

def Pillar(request):
    return render(request, 'neofi.html')


def Profile(request):
    userdata = UserDetail.objects.filter(usr=request.user).first()
    first = FirstTask.objects.filter(usr=request.user).first()
    skdata = UserSkills.objects.filter(usr=request.user).first()
    up = UserPort.objects.filter(usr=request.user).first()
    pdata = Project.objects.all()

    count = User.objects.count()
    if request.method == "POST":
        if 'projectname' in request.POST:
            ppd = datetime.today()
            Projectname = request.POST['projectname']
            Profiletitle = request.POST['projecttype']
            projectimg = request.FILES['projectimg']
            Project.objects.create(usr=request.user, ProjectName=Projectname, ProjectType=Profiletitle, ProjectImg=projectimg, ProjectPosted=ppd)
            return redirect('Profile')

        else:
            return redirect('Profile')

    return render(request, 'profile.html', {'userdata': userdata, 'first':first, 'count':count, 'skill':skdata, 'userport':up, 'pdata':pdata})

def EditProfile(request):
    userdata = UserDetail.objects.filter(usr=request.user).first()
    first = FirstTask.objects.filter(usr=request.user).first()
    skdata = UserSkills.objects.filter(usr=request.user).first()
    up = UserPort.objects.filter(usr=request.user).first()
    pdata = Project.objects.all()
    error = False

    if request.method == "POST":
        if 'img' in request.FILES:
            i = request.FILES['img']
            userdata.image = i
            userdata.save()
            return redirect('EditProfile')
        elif 'phone' in request.POST:
            phone = request.POST['phone']
            userdata.phone = phone
            userdata.save()
            return redirect('EditProfile')
        elif 'projectname' in request.POST:
            Projectname = request.POST['projectname']
            Profiletitle = request.POST['projecttype']
            projectimg = request.FILES['projectimg']
            Project.objects.create(usr=request.user, ProjectName=Projectname, ProjectType=Profiletitle, ProjectImg=projectimg)
            return redirect('EditProfile')

        elif 'skill' in request.POST:
            sk = request.POST['skill']
            UserSkills.objects.update(usr=request.user, Skills=sk)
            return redirect('EditProfile')

        elif 'Linkedin' in request.POST:
            linkedin = request.POST['Linkedin']
            UserPort.objects.update(usr=request.user, LinkedIn=linkedin)
            return redirect('EditProfile')
        elif 'Behance' in request.POST:
            linkedin = request.POST['Behance']
            UserPort.objects.update(usr=request.user, Behance=linkedin)
            return redirect('EditProfile')
        elif 'Instagram' in request.POST:
            linkedin = request.POST['Instagram']
            UserPort.objects.update(usr=request.user, Instagram=linkedin)
            return redirect('EditProfile')
        elif 'Twitter' in request.POST:
            linkedin = request.POST['Twitter']
            UserPort.objects.update(usr=request.user, Twitter=linkedin)
            return redirect('EditProfile')
        elif 'Github' in request.POST:
            linkedin = request.POST['Github']
            UserPort.objects.update(usr=request.user, Github=linkedin)
            return redirect('EditProfile')

        elif 'old' in request.POST:
            o = request.POST['old']
            n = request.POST['new']
            data = authenticate(usr=request.user.username, pas=o)
            if data:
                data.set_password(n)
                data.save()
                Logout(request)
                return SignIn(data)

            else:
                error = True
        else:
            return redirect('EditProfile')

    dis = {'userdata': userdata, 'first': first,  'skill': skdata, 'userport': up, 'error': error, 'pdata': pdata}
    return render(request, 'profile_edit.html', dis)


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
    return render(request, 'login.html', d)


def SignUp(request):
    error = False
    perror = False
    register = False
    if request.method == 'POST':
        dd = request.POST
        # ---Signup----
        '''
        u = dd['username']
        fn = dd['Firstname']
        ln = dd['Lastname']
        e = dd['email']
        p = dd['password']
        p1 = dd['password1']
        i = 'https://nichemodels.co/wp-content/uploads/2019/03/user-dummy-pic.png'
        td = date.today()
        '''
        #---Registration----
        q1 = dd['Q1']
        q2 = dd['Q2']
        q3 = dd['Q3']
        q4 = dd['Q4']
        q5 = dd['Q5']
        q6 = dd['Q6']
        q7 = dd['Q7']
        q8 = dd['Q8']
        q9 = dd['Q9']
        q10 = dd['Q10']

        udata = User.objects.filter(username=q2)
        if udata:
            error = True
        else:
            register = True
            # ---Signup----
            '''
            user = User.objects.create_user(username=u, password=p, email=e, first_name=fn, last_name=ln)
            UserDetail.objects.create(usr=user, image=i, EmailA=e, FirstN=fn, LastN=ln, JoinDate=td)
            UserSkills.objects.create(usr=user)
            UserPort.objects.create(usr=user, FirstN=fn, LastN=ln)
            '''
            user = User.objects.create_user(username=q2, password=q2, email=q2)
            FirstTask.objects.create(usr=user, Q1=q1, Q2=q2, Q3=q3, Q4=q4, Q5=q5, Q6=q6, Q7=q7, Q8=q8, Q9=q9, Q10=q10)
            return redirect('registration_s')



    d = {"error": error, 'perror': perror, 'register': register}
    return render(request, 'round0.html', d)

def Registration_S(request):
    return render(request,'recruitment/Registration_S.html')


def Logout(request):
    logout(request)
    return redirect('SignIn')




def AllProfile(request):

    adata= UserDetail.objects.filter(usr=request.user).first()
    udata = UserDetail.objects.all()
    return render(request, 'allprofile.html', {'udata':udata, 'adata':adata})

def Work(request):
    if request.user.is_authenticated:
        userdata = UserDetail.objects.filter(usr=request.user).first()
        pdata = Project.objects.all()

        d = {'userdata': userdata, 'project': pdata}

    else:
        pdata = Project.objects.all()
        d = {'project':pdata}

    return render(request, 'yourwork.html',d)

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


            if userdata.dept == 'Design':
                cdata = DesignAssignment.objects.get(id=n)
                DesignSubmit.objects.create(usr=request.user, AssignNo=cdata, Assignmentimng=i)
                return redirect('Yourtask')

            elif userdata.dept == 'Web':
                cdata = WebAssignment.objects.get(id=n)
                print(cdata)
                WebSubmit.objects.create(usr=request.user, AssignNo=cdata, Assignmentimng=i)
                return redirect('Yourtask')
            elif userdata.dept == 'App':
                cdata = AppAssignment.objects.get(id=n)
                AppSubmit.objects.create(usr=request.user, AssignNo=cdata, Assignmentimng=i)
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

    return render(request, 'task.html',{'userdata':userdata, 'assi':assi, 'design':design,})


def SingleProfile(request, pid):
    data = UserDetail.objects.get(id=pid)
    userdata = UserDetail.objects.filter(usr=request.user).first()
    skdata = UserSkills.objects.filter(usr=request.user).first()
    up = UserPort.objects.filter(usr=request.user).first()
    pdata = Project.objects.all()
    spdata = {'userdata': userdata,'skill':skdata, 'userport':up, 'data': data, 'pdata':pdata}
    return render(request, 'singleprofile.html', spdata)

