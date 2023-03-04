from django.db import models
from hire.models import jobPost
# Create your models here.

class docs(models.Model):
    app_id = models.AutoField(primary_key=True)
    fk = models.ForeignKey("hire.jobPost", verbose_name=("Foreign Key"), on_delete=models.CASCADE,default = None)
    first_name = models.CharField(max_length=20,default=None,null=True)
    last_name = models.CharField(max_length=20,default=None,null=True)
    files_resume = models.FileField(upload_to="jobs/resume/",null=True,default=None)
    files_cl = models.FileField(upload_to="jobs/CoverLetters/",null=True,default=None)
    user_id = models.IntegerField(default=None)