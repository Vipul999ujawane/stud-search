from django.contrib import admin
from .models import Stud
# Register your models here.

class StudAdmin(admin.ModelAdmin):
    list_display=('roll','name','hall')
    search_fields=('roll','name','hall')
admin.site.register(Stud,StudAdmin)
