from django import forms
from .models import Job

class JobForms(forms.ModelForm):

    class Meta:
        model=Job
        fields=[
            'title' ,
            'description' ,
            'requirements',
            'location'
            'salary' ,
            'category',
            'job_type',
            'experience_level',
            'mode',
            'application_deadline'
        ]