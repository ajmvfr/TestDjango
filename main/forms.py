from django import forms
from .models import Announcement
from django.core.exceptions import ValidationError
# from ckeditor.widgets import CKEditorWidget
# from django_ckeditor_5.widgets import CKEditor5Widget
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class AnnouncementForm(forms.ModelForm):
    # title = forms.CharField(max_length=200)
    # text = forms.CharField(widget=CKEditorWidget())
    # expire_date = forms.DateField()
    # active = forms.BooleanField()
    # due_date = forms.DateField()
    # sort_order =forms.IntegerField()
    class Meta:
        model = Announcement
        fields = '__all__'
        exclude = ('organization',)
        widgets = {
            'text': SummernoteWidget(),
            # 'bar': SummernoteInplaceWidget(),
        }
        # widgets = {
        #       "text": CKEditor5Widget(
        #           attrs={"class": "django_ckeditor_5"}, config_name="comment"
        #       )
        # }
    