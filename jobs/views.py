from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from  django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import job,Application
from .forms import Jobform
# Create your views here.

class JobListView(ListView):
    model = job
    template_name = 'job_list.html'
    context_object_name = 'all_jobs'
    ordering = ["-date_posted"]

class JobDetailView(DeleteView):
    model= job
    template_name = 'job_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context['already_applied']= Application.objects.filter(job = self.object, applicant=self.user).exists()
            return context

class JobCreateView(LoginRequiredMixin,CreateView):
    model = job
    form_class = Jobform
    template_name = "job_form.html"
    success_url = reverse_lazy("my_jobs")

    def form_valid(self, form):
        form.instance.Posted_by = self.request.user
        messages.success(self.request,("Job created successfully!"))
        return super().form_valid(form)

class JobUpdateView(LoginRequiredMixin,UpdateView):
    model = job
    form_class = Jobform
    template_name = "job_form.html"
    success_url = reverse_lazy("my_jobs")

    def get_queryset(self):
        return job.objects.filter(posted_by=self.request.user)

class JobDeleteView(LoginRequiredMixin,DeleteView):
    model = job
    template_name = "job_confirm_delete.html"
    success_url = reverse_lazy("my_jobs")

    def get_queryset(self):
        return job.objects.filter(posted_by=self.request.user)

class MyJobsListView(LoginRequiredMixin,ListView):
    model = job
    template_name = "my_jobs.html"
    context_object_name = "jobs"

    def get_queryset(self):
        return job.objects.filter(posted_by=self.request.user).order_by("-date_posted")

@login_required
@require_POST
def apply_to_job(request,pk):
    job = get_object_or_404(job,pk=pk)

    application,created= application.objects.get_or_create(job=job,applicant=request.user,)

    if created:
        messages.success(request,"Application submited successfully!")
    else:
        messages.info(request,"You already applied for this post")

        return redirect("my_applications")

class MyApplicationListView(LoginRequiredMixin,ListView):
    model = Application
    template_name = "my_application.html"
    context_object_name = "applications"

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user).select_related("job").order_by("-date_applied")
    
        
        
        