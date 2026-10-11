from django.contrib import admin
from .models import job,Application

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ['title','Company_name','location','salary','posted_by','date_posted']
    search_fields = ['title','Company_name']
    list_filter = ['location']

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant','job','date_applied']

admin.site.register(job,JobAdmin)
admin.site.register(Application,ApplicationAdmin)
