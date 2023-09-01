from django.db import models
from django.db.models.signals import pre_save
# Create your models here.

class Student(models.Model):

    first_name= models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email_id = models.EmailField(max_length=30)
    phone_no=models.CharField(max_length=13,primary_key=True)
    course=models.CharField(max_length=20)

    def __str__(self) :
        return self.first_name
    
def presignal (sender,instance,*args,**kwargs):
    print('signal recived')
    print(sender)
    print(instance.first_name,instance.last_name,instance.phone_no,instance.course)

pre_save.connect(presignal,Student) 


class Python(models.Model):

    first_name= models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email_id = models.EmailField(max_length=30)
    phone_no=models.CharField(max_length=13,primary_key=True)
    course=models.CharField(max_length=20)

    def __str__(self) :
        return self.first_name

class Java(models.Model):

    first_name= models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email_id = models.EmailField(max_length=30)
    phone_no=models.CharField(max_length=13,primary_key=True)
    course=models.CharField(max_length=20)

    def __str__(self) :
        return self.first_name

class Testing(models.Model):

    first_name= models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email_id = models.EmailField(max_length=30)
    phone_no=models.CharField(max_length=13,primary_key=True)
    course=models.CharField(max_length=20)

    def __str__(self) :
        return self.first_name

class python_joiners(models.Model):

    names=models.CharField(max_length=30)
    username=models.CharField(max_length=20)
    password= models.CharField(max_length=15)
    email_id=models.EmailField(max_length=20)
    phone_no=models.CharField(max_length=10)
    course=models.CharField(max_length=15)

    def __str__(self) :
        return self.name

class java_joiners(models.Model):

    name=models.CharField(max_length=30)
    username=models.CharField(max_length=20)
    password= models.CharField(max_length=15)
    email_id=models.EmailField(max_length=20)
    phone_no=models.CharField(max_length=10)
    course=models.CharField(max_length=15)

    def __str__(self) :
        return self.name

class testing_joiners(models.Model):

    name=models.CharField(max_length=30)
    username=models.CharField(max_length=20)
    password= models.CharField(max_length=15)
    email_id=models.EmailField(max_length=20)
    phone_no=models.CharField(max_length=10)
    course=models.CharField(max_length=15)

    def __str__(self) :
        return self.name
