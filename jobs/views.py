from django.shortcuts import render
from django.views import generic
# Create your views here.
from users.mixins import PosterRequiredMixin
from .models import Job,Location
from django.http import JsonResponse
def home(request):
    locations=Location.choices
    loc=[]
    for i in locations:
        loc.append(i[1])
    return render(request,'home.html',{'locations':loc})

def get_all_locations(request):
    locations=Location.choices
    loc=[]
    for i in locations:
        loc.append(i[1])
    return JsonResponse({'locations':loc})

class CreateJobView(PosterRequiredMixin,generic.CreateView):
    model = Job
    login_url='/'
    fields = ['title', 'description', 'requirements', 'location', 'salary', 'category', 'job_type', 'experience_level', 'mode', 'application_deadline']
    template_name = 'job/job_form.html'
    success_url='/jobs/'

    def form_valid(self, form):
        form.instance.poster = self.request.user 
        return super().form_valid(form)
    
class ListJobsView(generic.ListView):
    model=Job
    template_name='job/job_list.html'

class JobDetailsView(generic.DetailView):
    model=Job
    template_name='job/job_details.html'
