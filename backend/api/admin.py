from django.contrib import admin

# Register your models here.

from api.models import Student

class apiAdmin (admin.ModelAdmin) :
    list_display = ("name", "age", "email")
admin.site.register(Student, apiAdmin)

# step 2