from django.contrib import admin
from registration.models import Professional
# Register your models here.

# class ProfessionalAdmin(admin.ModelAdmin):
#     fields= [""]

admin.site.register(Professional)
