from .models import student_list
from django import forms

class StudentsForm(forms.ModelForm):
    
    class Meta: #provide the information
        model=student_list
        fields='__all__'