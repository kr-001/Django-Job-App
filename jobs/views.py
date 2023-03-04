from django.shortcuts import render

# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
from .models import docs
from django.core.files.storage import FileSystemStorage
from .forms import updateJob
from hire.models import jobPost,accepted,deleted
def index(request):
    item = jobPost.objects.all()
    print(item)
    return render(request,'jobs/index.html',{'job':item})

def showJobs(request,id):
    title = jobPost.objects.filter(job_id = id)[0]
    print(title)
    return render(request , 'jobs/jobPost.html' , {'item':title })

def register(request):
    if request.method=='POST':
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username=request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2= request.POST.get('pass2')
        # print(User.objects.filter(username=username))
        
        if pass1==pass2:
          if User.objects.filter(email=email).exists():
            messages.info(request,'Email already in use')
            return redirect('/jobs',{'messages':messages})
          elif User.objects.filter(username=username).exists():
            messages.info(request,'Username already taken,Try diffrent one')
            return redirect('/jobs',{'messages' : messages})
          else:
            user = User.objects.create_user(email=email,first_name = fname,last_name = lname,username=username,password=pass1)
            user.save();
            messages.info(request,'Success Registration,Login to continue')
            return redirect('/jobs/login',{'messages': messages})
    else:
        return render(request,'jobs/index.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password =request.POST['pass1']

        user  = authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['username'] = username
            request.session.set_expiry(200)
            return redirect('/jobs')
        else:
            messages.info(request,"Aunthentication Failed,Check provided credentials")
            return redirect('/jobs/login',{'messages': messages})
    else:
        return render(request,'jobs/login.html')
    
def logout_user(request):
    try:
        logout(request)
        del request.session['username']
    except KeyError:
       pass
    return redirect('/jobs')



def upload(request,id):
   list = jobPost.objects.filter(job_id = id)[0]
   if request.method == "POST":
      form = updateJob(request.POST,request.FILES)
      if form.is_valid():
         instance = form.save(commit=False)
         data = jobPost.objects.filter(job_id = id)[0]
         curr_user = request.user
         instance.fk = data
         instance.user_id = curr_user.id
         instance.save()
         return redirect('/jobs/')
   else:
      form = updateJob()
   return render(request , 'jobs/upload.html/',{'form':form , 'job' : list})


def profile(request):
    curr_user = request.user.id
    jobs = accepted.objects.filter(sno = curr_user)
    user_job = []
    for job in jobs:
       user_job.append(job)
    print(user_job)
    rejected = deleted.objects.filter(sno = curr_user)
    rej_job = []
    for job in rejected:
       rej_job.append(job)
    print(rej_job)
    return render (request , 'jobs/profile.html' , {'jobs' : user_job , 'rej' : rej_job})

    

          
      
      