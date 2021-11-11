from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(StudentUser)

# @admin.register(StudentUser)
class StudentUserAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'mobile', 'image', 'gender', 'type', 'resume')

admin.site.register(StudentUser, StudentUserAdmin)

