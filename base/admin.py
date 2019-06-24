from django.contrib import admin
from .models import *
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display = ['title','category','author','source_url']
admin.site.register(Blog, BlogAdmin)