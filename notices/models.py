from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from datetime import datetime 


class Notices(models.Model):
    notice_title = models.CharField(max_length=150)
    notice_sender = models.CharField(max_length=50)
    notice_slug = AutoSlugField(
        populate_from='notice_title',  unique=True,  null=True, default=None)
    notice_img = models.FileField(
        upload_to="notices/", max_length=250, null=True, default=None)
    notice_date = models.DateTimeField(default=datetime.now)
    # notice_date = models.DateTimeField(auto_now_add=True, blank=True)
    notice_description = HTMLField()
