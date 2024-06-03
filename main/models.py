from django.db import models
from datetime import datetime, date
import uuid
from django.urls import reverse
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
# from django_ckeditor_5.fields import CKEditor5Field

class Announcement(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # text = models.CharField(max_length=50000, blank=True, null=True)
    # text=CKEditor5Field(null=True,blank=True, config_name='default')
    # text = RichTextField(blank=True, null=True)
    # media_field = RichTextUploadingField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    publish_date = models.DateField(default=date.today)
    expire_date = models.DateField(null=True,blank=True)
    active = models.BooleanField(default=True)
    due_date = models.DateField(null=True,blank=True)
    sort_order = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("announcements:edit-announcement", kwargs={"announcement_id": self.id})

    def delete_object(self):
         return reverse('announcements:delete-announcement', kwargs={"announcement_id": self.id})
     