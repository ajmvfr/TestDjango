from django.urls import path
from . import views

app_name = 'announcements'

urlpatterns = [
    path('announcements/', views.announcements, name="announcements"),
    path('add-announcement/', views.download_add_files, name='add-announcement'),    
    path('list-announcement/',views.ListAnnouncement.as_view() , name="list-announcement"),
    path('delete-announcement/<str:announcement_id>/', views.AnnouncementDeleteView.as_view(), name='delete-announcement'),
    path('edit-announcement/<str:announcement_id>/', views.announcement_edit_files, name='edit-announcement'),    
]

