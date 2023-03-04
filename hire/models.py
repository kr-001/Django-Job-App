from django.db import models
from datetime import datetime

class jobPost(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=50,default='0')
    company_name = models.CharField(max_length=50,default='0')
    location = models.CharField(max_length=50,default='0')
    salary = models.CharField(max_length=50,default='0')
    experience = models.CharField(max_length=50,default='0')
    pub_date = models.DateTimeField(datetime.now(),null=True)
    job_description = models.CharField(max_length=50,default='00')
# Create your models here.

    def __st__(self)->str:
        return self.job_id
class accepted(models.Model):
    sno = models.IntegerField(primary_key=True)
    fk = models.ForeignKey('jobPost' , on_delete=models.CASCADE)
    title = models.CharField(max_length=50,default=None)
    name = models.CharField(max_length=50,default=None,null=True)
    resume = models.FileField(upload_to='jobs/accepted/resumes',max_length=50,default=None)
    coverLetter = models.FileField(upload_to='jobs/accepted/covers',max_length=50,default=None)

class deleted(models.Model):
    sno = models.IntegerField(primary_key=True)
    fk = models.ForeignKey('jobPost' , on_delete=models.CASCADE)
    title = models.CharField(max_length=50,default=None)
    name = models.CharField(max_length=50,default=None,null=True)
    resume = models.FileField(upload_to='jobs/deleted/resumes',max_length=50,default=None)
    coverLetter = models.FileField(upload_to='jobs/delete/covers',max_length=50,default=None)