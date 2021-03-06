"""student_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accounts import views as v

urlpatterns = [
    
    path('',v.home),

    #path('student_list',v.student_list,name="student_list"),
    path('add_student_page',v.add_student_page,name="add_student_page"),
    path('add_student',v.add_student,name="add_student"),
    path('edit_student/<int:id>',v.edit_student,name="edit_student"),
    path('delete_student/<int:id>',v.delete_student),
]
