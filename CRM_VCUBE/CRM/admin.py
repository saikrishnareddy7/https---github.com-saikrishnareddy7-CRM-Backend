from django.contrib import admin
from .models import Student,Python,Java,Testing,python_joiners,java_joiners,testing_joiners

# Register your models here.

class stuadmin(admin.ModelAdmin):
    
    list_display=['first_name','last_name','course','email_id']
    search_fields=['first_name','last_name']
    list_filter=['first_name','last_name','course']
    


admin.site.register(Student,stuadmin)
admin.site.register(Python)
admin.site.register(Java)
admin.site.register(Testing)
admin.site.register(python_joiners)
admin.site.register(java_joiners)
admin.site.register(testing_joiners)