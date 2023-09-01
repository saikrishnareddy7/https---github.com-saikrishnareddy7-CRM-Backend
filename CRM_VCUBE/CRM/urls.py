from django.urls import path
from.import views


urlpatterns=[
    path('',views.home,name='homepageform' ),
    path('enroll/',views.enroll, name='enrollform' ),
    path('adminslogin/',views.adminlogin,name='adminlogin'),
    path('admins/',views.admins, name='adminpage'),
    path('enrolled_student/',views.select, name='all_enrolled'),
    path('python_students/',views.Python_student,name='python_enrolled'),
    path('java_students/',views.java_student,name='java_enrolled'),
    path('testing_students/',views.testing_students,name='testing_enrolled'),
    path('python_joiners/',views.python_joiner,name='python_joiners'),
    path('signals/',views.signalfun,name='signalfun'),

]
'''name=homepageform == home page'''

'''name=enrollform == enroll form page'''

'''name=adminlogin ==  admin login page'''

'''name=adminpage ==  admin home page'''

'''name= all_enrolled==  all enrolled students will appear'''

'''name=python_enrolled == all python enrolled students will appear'''

'''name=java_enrolled == all java enrolled students will appear'''

'''name=testing_enrolled == all testing enrolled students will appear'''


