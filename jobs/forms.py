from .models import docs
from django.forms import ClearableFileInput
from django import forms
# from hire.models import docs
class updateJob(forms.ModelForm):
    class Meta:
        model = docs
        fields = ['fk','first_name','last_name','files_resume','files_cl','user_id']
        exclude = ['fk','user_id']