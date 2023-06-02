from django.contrib import admin
from .models import Student,Cleaner
# Register your models here.


admin.site.register(Student)
admin.site.register(Cleaner)
                    

class StudentAdmin(admin.ModelAdmin):
    list_display = ['s_Name', 's_Registration_Number', 's_Block']
    list_filter = ['s_Block', 's_Name']
    search_fields = ['s_Name', 's_Registration_Number']


class CleanerAdmin(admin.ModelAdmin):
    list_display = ['c_Name', 'c_Registration_Number', 'c_Block']
    list_filter = ['c_Block']
    search_fields = ['c_Name', 'c_Registration_Number']