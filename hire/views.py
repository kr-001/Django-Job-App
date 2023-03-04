from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
from .models import jobPost,accepted,deleted
from jobs.models import *
from django.contrib.auth.decorators import login_required
from django.template import loader
from os import listdir
from django.conf import settings
from django.views.generic.base import TemplateView

@login_required(login_url='/hire/login')
def index(request):
    data = jobPost.objects.all()
    print(data)
    job = {'job' : data}
    return render(request,'hire/index.html',job)

def showJob(request,id):
    title = jobPost.objects.filter(job_id = id)[0]
    return render(request , 'hire/jobpost.html' , {'item' : title})

def register(request):
    if request.method=='POST':
        email = request.POST['email']
        username=request.POST['username']
        pass1 = request.POST['pass1']
        pass2= request.POST['pass2']
        # print(User.objects.filter(username=username))
      
        if pass1==pass2:
          if User.objects.filter(email=email).exists():
            messages.info(request,'Email already in use')
            return redirect('/hire',{'messages':messages})
          elif User.objects.filter(username=username).exists():
            messages.info(request,'Username already taken,Try diffrent one')
            return redirect('/hire',{'messages' : messages})
          else:
            user = User.objects.create_user(email=email,username=username,password=pass1)
            user.save();
            messages.info(request,'Success Registration,Login to continue')
            return redirect('/hire/login',{'messages': messages})
    else:
        return render(request,'hire/index.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password =request.POST['pass1']

        user  = authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['username'] = username
            request.session.set_expiry(200)
            return redirect('/hire')
        else:
            messages.info(request,"Aunthentication Failed,Check provided credentials")
            return redirect('/hire/login',{'messages': messages})
    else:
        return render(request,'hire/login.html')
  
def logout_user(request):
    try:
        logout(request)
        del request.session['username']
    except KeyError:
       pass
    return redirect('/hire')

def createJob(request):
    if request.method=='POST':
        job_title = request.POST.get('role_name')
        company_name = request.POST.get('company')
        location = request.POST.get('location')
        salary = request.POST.get('salary')
        exp = request.POST.get('exp')
        desc = request.POST.get('desc')
        branch = request.POST.get('branch')
        job=jobPost(job_title = job_title , company_name = company_name , location = location , salary = salary , experience = exp,job_description = desc,branch = branch)
        job.save()
        return redirect('/hire')
    else:
        return render(request,'hire/create_job.html')


def dashboard(request):
    data = jobPost.objects.all()
    print(data)
    
    # person = accepted.objects.all()
    # print('persons->>>>',person)
    job = {'job' : data }
    return render(request,'hire/dashboard.html',job)

def applications(request,id):
    # app = docs.fk
    # obj = app.get_queryset(job_id = id)
    # print(obj)
    # data = obj.filter(job_id = id)[0]
    # print(data)
    x = docs.objects.filter(fk = id)
    print(x)
    #template = loader.get_template('jobapp/hire/templates/hire/applications.html')
    context = {
        'data' : x
    }
    
    return render(request , 'hire/applications.html' , context)

def accept(request,id):
    obj = docs.objects.filter(app_id = id)
    first_name = obj[0].first_name
    last_name = obj[0].last_name
    print(obj)
    x = obj[0].fk
    jobName = x.job_title
    print(x.job_id)
    # print(first_name , last_name)
    name = first_name + last_name
    resume = obj[0].files_resume
    cover = obj[0].files_resume
    y = docs.objects.all()[0].user_id
    data = accepted(sno = y ,fk = x,title = jobName,name = name , resume = resume, coverLetter = cover)
    data.save()
    docs.objects.filter(app_id = id).delete()
    #Show Hired Peoples from Accepted Model
    person = accepted.objects.all()
    print('persons->>>>',person)
    return render(request , 'hire/dashboard.html',{'person':person})


def delete(request,id):
    obj = docs.objects.filter(app_id = id)
    first_name = obj[0].first_name
    last_name = obj[0].last_name
    print('obj',obj)
    x = obj[0].fk
    jobName = x.job_title
    print(x.job_id)
    print(first_name , last_name)
    name = first_name + last_name
    resume = obj[0].files_resume
    cover = obj[0].files_resume
    y = docs.objects.all()[0].user_id
    data = deleted(sno = y,fk = x,title = jobName,name = name , resume = resume, coverLetter = cover)
    data.save()
    docs.objects.filter(app_id = id).delete()
    #Show Hired Peoples from Accepted Model
    person = accepted.objects.all()
    print('persons->>>>',person)
    return render(request , 'hire/dashboard.html',{'person':person})
    
def hired(request):
    person = accepted.objects.all()
    return render(request,'hire/dashboard.html',{'person' : person})

def delete_job(request,id):
    job = jobPost.objects.filter(job_id = id)
    job.delete()
    jobs = jobPost.objects.all()
    return redirect('/hire/dashboard' ,{'job' : jobs} )


def modify_job(request,id):
    if request.method == "POST":
        job = jobPost.objects.get(job_id = id)
        title = request.POST.get('title')
        cname = request.POST.get('cname')
        loc = request.POST.get('loc')
        sal = request.POST.get('sal')
        exp = request.POST.get('exp')
        job.job_title = title
        job.company_name = cname
        job.location = loc
        job.salary = sal
        job.experience = exp
        job.save()

        return redirect('/hire/')
    else:
        m = messages.error(request , "Error Occured")
        return render(request , 'hire/index.html' , {'msg' : m})

def update_record(request,id):
    job = jobPost.objects.filter(job_id = id)[0]
    print(job)
    return render(request , 'hire/updateRecord.html',{'job' : job})

def search(request):
    search_d = request.GET['search']
    data = jobPost.objects.filter(job_title__contains=search_d)
    print(data)
    return render(request , 'hire/index.html' , {'job' : data})


def admin(request):
    return render(request,'hire/admin.html')