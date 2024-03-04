from django.contrib import admin
from .models import Mentor,Student,Adminstration,AbsentReason

# Register your models here.
admin.site.register(Mentor)
admin.site.register(Student)
admin.site.register(Adminstration)
admin.site.register(AbsentReason)
