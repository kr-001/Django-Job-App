from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('' , views.index , name ="candidtehome"),
    path('register',views.register,name='register'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('jobPost/<int:id>',views.showJobs,name='showJobs'),
    path('upload/<int:id>',views.upload,name='upload'),
    path('profile',views.profile,name='profile')

    #  path('createJob',views.createJob,name='createJob'),


   
]
