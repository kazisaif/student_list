from django.shortcuts import render,redirect
from accounts.form import StudentsForm

from accounts.models import student_list

# Create your views here.
def home(request):
    slist=student_list.objects.all()
    context={'slist':slist}
    return render(request,"home.html",context)

####### Book Section ############

def add_student_page(request):
    return render(request,"add_student.html")

def add_student(request):
    
    student_id=request.POST.get('student_id')
    student_name=request.POST.get('student_name')
    student_dept=request.POST.get('student_dept')
    student_email=request.POST.get('student_email')
    student_mobile=request.POST.get('student_mobile')
    student_address=request.POST.get('student_address')
    
    asl=student_list()
    asl.student_id=student_id
    asl.student_name=student_name
    asl.student_department=student_dept
    asl.student_email=student_email
    asl.student_mobile=student_mobile
    asl.student_address=student_address
    asl.save()
        
    return redirect('/')
    
def edit_student(request,id):
    bid=student_list.objects.get(id=id)
    
    if request.method=='POST':
        sf=StudentsForm(request.POST,instance=bid)
        sf.save()
        #return render(request,'movielist.html')
        return redirect("/")
    else:
        #m.error(request,'Try Again...')
        sf=StudentsForm(instance=bid)
        context={'form':sf}
        return render(request,"edit_student.html",context)

def delete_student(request,id):
    sid=student_list.objects.get(id=id)
    sid.delete()
    return redirect("/")