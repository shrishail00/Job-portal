from django.urls import path

from .views import(
    JobListView,
    JobDetailView,
    JobCreateView,
    JobUpdateView,
    JobDeleteView,
    MyJobsListView,
    MyApplicationListView,
    apply_to_job,
)

urlpatterns = [
    
    path("", JobListView.as_view(), name="job_list"),
    path("<int:pk>/", JobDetailView.as_view(), name="job_detail"),
    path("my-jobs/", MyJobsListView.as_view(), name="my_jobs"),
    path("create/", JobCreateView.as_view(), name="job_create"),
    path("<int:pk>/update/", JobUpdateView.as_view(), name="job_update"),
    path("<int:pk>/delete/", JobDeleteView.as_view(), name="job_delete"),
    path("<int:pk>/apply/", apply_to_job, name="apply_to_job"),
    path(
        "my-applications/",
        MyApplicationListView.as_view(),
        name="my_applications",
    ),
]