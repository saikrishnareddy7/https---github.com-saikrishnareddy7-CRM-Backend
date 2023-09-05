from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from. models import Student,Python,Java,Testing,python_joiners
from django.contrib import messages
from .forms import Enrollform
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    
    '''if request.method == 'POST':'''

        
    return render(request,'homepage.html')


def enroll(request):

    fobj = Enrollform()

    if request.method == 'POST':
        f_name=request.POST['first_name']
        l_name=request.POST['last_name']
        email=request.POST['email_id']
        phone=int(request.POST['phone_no'])
        subject=request.POST['intrest']

        if request.POST['intrest'] =='python':
            Python.objects.create(first_name=f_name,last_name=l_name,email_id=email,phone_no=phone,course=subject)
            Student.objects.create(first_name=f_name,last_name=l_name,email_id=email,phone_no=phone,course=subject)
            messages.success(request, ' {} {} you are enrolled for PYTHON DEMO successfully in VCUBE SOFTWARE SOLUTIONS,' .format(f_name,l_name))
            messages.success(request,' we will contact you as soon as possible')

            return render (request,'enroll.html',{'form':fobj})
        
        elif request.POST['intrest'] =='java':

            Java.objects.create(first_name=f_name,last_name=l_name,email_id=email,phone_no=phone,course=subject)
            Student.objects.create(first_name=f_name,last_name=l_name,email_id=email,phone_no=phone,course=subject)
            messages.success(request, ' {} {} you are enrolled for JAVA DEMO successfully in VCUBE SOFTWARE SOLUTIONS,' .format(f_name,l_name))
            messages.success(request,' we will contact you as soon as possible')

            return render (request,'enroll.html',{'form':fobj})
        
        else:

            Testing.objects.create(first_name=f_name,last_name=l_name,email_id=email,phone_no=phone,course=subject)
            Student.objects.create(first_name=f_name,last_name=l_name,email_id=email,phone_no=phone,course=subject)
            messages.success(request, ' {} {} you are enrolled for TESTING TOOLS successfully in VCUBE SOFTWARE SOLUTIONS,' .format(f_name,l_name))
            messages.success(request,' we will contact you as soon as possible')

            return render (request,'enroll.html',{'form':fobj})
        
    return render (request,'enroll.html',{'form':fobj})


def signalfun(request):
    return HttpResponse(request,'signal recivied')

def python_joiner(request):
    

    if request.method == 'POST':

        f_name=request.POST['fullname']
        u_name=request.POST['username']
        p_word=request.POST['password']
        email=request.POST['email_id']
        phone_no=int(request.POST['phone_no'])
        subject=request.POST['intrest']


        python_joiners.objects.create(names=f_name,username=u_name,password=p_word,email_id=email,phone_no=phone_no,course=subject)
        return render(request,'python_joiners.html')

    return render(request,'python_joiners.html')


def adminlogin(request):

    if request.method == 'POST':

        uname=request.POST['uname']
        pswd=request.POST['pwd']

        valid_user = authenticate(request,username=uname,password=pswd)

        if valid_user != None:

            return redirect('adminpage')
        else:
            messages.error(request,'INVALID CREDENTIALS')
            messages.error(request,'PLEASE CHECK THE CREDENTIALS')
            return render(request,'adminlogin.html')

    return render(request,'adminlogin.html')

    
@login_required(login_url='adminlogin')
def admins(request):

    return render(request,'admins.html')

def select (request):
    
    students=Student.objects.all()


    return render(request,'enrolled_students.html',{'student':students})

def Python_student(request):

    python_students=Python.objects.all()

    return render(request,'python_students.html',{'p_student':python_students})

def java_student(request):
    
    java_students=Java.objects.all()

    return render(request,'java_students.html',{'j_student':java_students})

def testing_students(request):
    
    testing_students=Testing.objects.all()

    return render(request,'testing_students.html',{'t_student':testing_students})
