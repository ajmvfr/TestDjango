from django.shortcuts import render, redirect
from .models import Announcement
from datetime import date, timedelta
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .forms import AnnouncementForm

def announcements(request):

    announcements = Announcement.objects.filter(
           Q(active=True) & 
           Q(publish_date__lte=date.today()) & 
           (Q(expire_date__gte=date.today())| Q(expire_date=None))
           ).all().order_by('sort_order','created_on')
    context = {'announcements': announcements,
               }
    return render(request, 'main/home.html', context)

class ListAnnouncement(LoginRequiredMixin, ListView):
    template_name = 'main/announcements_list.html'
    paginate_by = 20
    
    def get_queryset(self):
        # title_slug = self.kwargs.get('slug')
        events = Announcement.objects.all()
        return events


    
# class AnnouncementEditView(LoginRequiredMixin, UpdateView):
#     model = Announcement
#     template_name = 'main/announcement_maint_form.html'
#     form_class = AnnouncementForm
#     success_url = '/list-announcement/'
#     pk_url_kwarg = 'announcement_id'
    
    
def announcement_edit_files(request, announcement_id):
    announcements = Announcement.objects.get(id=announcement_id)
    print(f'---{announcements.title}')
    form = AnnouncementForm(instance=announcements)
    if request.POST:
        form = AnnouncementForm(request.POST, instance=announcements)
        # form = AnnouncementForm(request.POST)
        # print(f'===={request.POST}')
        # form = AnnouncementForm(request.POST, request.FILES, instance=announcements)
        if form.is_valid():
            announce = form.save(commit=False)
            print(f'===={announce.text}')
            announce.save()
        return redirect('announcements:list-announcement')
    
    context = {
        'form': form
        }
    return render(request, 'main/announcement_maint_form.html',context)

def download_add_files(request):
    form = AnnouncementForm()
    if request.POST:
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announce = form.save(commit=False)
            announce.save()
        return redirect('announcements:list-announcement')
    
    context = {
        'form': form
        }
    return render(request, 'main/announcement_maint_form.html',context)
        
 
# class AnnouncementAddView(LoginRequiredMixin, CreateView):
#     model = Announcement
#     template_name = 'main/announcement_maint_form.html'
#     form_class = AnnouncementForm
#     success_url = '/list-announcement/'
    

#     def post(self, request, *args, **kwargs):
#         form = AnnouncementForm(request.POST)
#         if form.is_valid():
#             event = form.save(commit=False)
#             event.save()
#             return redirect('announcements:list-announcement')
#         else:
#             return self.form_invalid(form)


class AnnouncementDeleteView(LoginRequiredMixin, DeleteView):
    model = Announcement
    template_name = 'main/confirm-delete.html'
    success_url = '/list-announcement/'
    pk_url_kwarg = 'announcement_id'    
    

 