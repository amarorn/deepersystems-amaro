from django.contrib import admin
from videos.models import *

class VideoAdmin(admin.ModelAdmin):
    fields = ('video','name','theme')
    list_display = ['name','video']
    search_fields = ['name']


# Register your models here.
admin.site.register(Video,VideoAdmin)