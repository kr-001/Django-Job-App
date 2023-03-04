
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('' , views.index , name ="hirehome"),
    path('jobpost/<int:id>' , views.showJob , name ="showJob"),
    path('register',views.register,name='register'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
     path('create_job',views.createJob,name='createJob'), 
     path('dashboard',views.dashboard,name='dashboard') ,
    #  path('dashboard',views.hired,name='dashboard') ,
     path('applications/<int:id>' , views.applications,name='applications'),
     path('accept/<int:id>', views.accept , name='accept'),
     path('delete/<int:id>', views.delete , name='delete'),
]
