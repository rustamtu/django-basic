from django.contrib import admin
from notices.models import Notices
# Register your models here.

class NoticeAdmin(admin.ModelAdmin):
    list_display=('id','notice_slug','notice_title', 'notice_sender', 'notice_img',)
    
admin.site.register(Notices, NoticeAdmin)