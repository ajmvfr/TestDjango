from django.contrib import admin
from .models import Announcement
from django_summernote.admin import SummernoteModelAdmin

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title','text','publish_date','expire_date','due_date','active','sort_order')
    search_fields = ['title']
    summernote_fields = ('text',)

class AnnouncementAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)   

# admin.site.register(Announcement,AnnouncementAdmin)

admin.site.register(Announcement,AnnouncementAdmin)
