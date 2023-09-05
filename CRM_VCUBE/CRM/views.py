from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from. models import Student,Python,Java,Testing,python_joiners
from django.contrib import messages
from .forms import Enrollform
from django.contrib.auth import authenticate,logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.
def home(request):
    
    '''if request.method == 'POST':'''

        
    return render(request,'homepage.html')


def studentpage(request):
    if request.method == 'POST':
        user=request.POST['username']
        password=request.POST['pasword']

        valid_user = authenticate(request,username=user,password=password)

        if valid_user != None:
            
            return render(request,'studentpage.html')



    return render(request,'studentlogin.html')


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
        sub=request.POST['intrest']

        #user_check = authenticate(request,username=u_name,password=p_word,email_id=email,phone_no=phone_no)

        if not python_joiners.objects.filter(email_id=email,phone_no=phone_no).exists():

            if  python_joiners.objects.filter(username=u_name).exists():
                messages.success(request,'*{}* username already exist please add any other else'.format(u_name))
            
            else:
                subject ='you are joined in vcube'
                message ='hi {f_name} iam sample mail  its student registration'
                from_email=settings.EMAIL_HOST_USER
                recipient_list=[email]
                send_mail(subject,message,from_email,recipient_list)

                python_joiners.objects.create(names=f_name,username=u_name,password=p_word,email_id=email,phone_no=phone_no,course=sub)
                messages.success(request,'{} joined in vcube'.format(f_name))

                user = User.objects.create_user(username=u_name,email=email,password=p_word)
                user.save()


                return render(request,'python_joiners.html')
        else:
            messages.success(request,'{} already joined in vcube'.format(f_name))


    return render(request,'python_joiners.html')


def adminlogin(request):

    if request.method == 'POST':

        e_mail=request.POST['mail']
        uname=request.POST['uname']
        pswd=request.POST['pwd']

        valid_user = authenticate(request,username=uname,password=pswd)

        if valid_user != None:
            

            #subject ='you are loged in to vcube'
            #message ='hi {uname} iam sample mail  its admin login'
            #from_email=settings.EMAIL_HOST_USER
            #recipient_list=[e_mail]
            #send_mail(subject,message,from_email,recipient_list)

            if request.user.is_superuser:
                
                return render(request,'studentpage.html')
            
            
            if request.user.is_active:
                
                return render(request,'admins.html')
            
           
           
        else:
            messages.error(request,'INVALID CREDENTIALS')
            messages.error(request,'PLEASE CHECK THE CREDENTIALS')
            return render(request,'adminlogin.html')

    return render(request,'adminlogin.html')

    
@login_required(login_url='adminlogin')
def admins(request):

    return render(request,'admins.html')

def logout(request):
    logout(request)
    return redirect('adminlogin')

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
