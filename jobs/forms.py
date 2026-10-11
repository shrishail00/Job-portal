from django import forms
from .models import job

class Jobform(forms.ModelForm):
    class Meta:
        model = job
        fields = ['title','Company_name','description','location','salary']
        