from django.urls import path
from .views import DashboardView
from .apps import TeacherConfig
from user.decorators import teacher_required

app_name = TeacherConfig.name

urlpatterns = [
    path("dashboard/", teacher_required(DashboardView.as_view()), name="dashboard"),
]
