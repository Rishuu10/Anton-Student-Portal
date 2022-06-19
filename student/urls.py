from django.urls import path
from .views import DashboardView
from .apps import StudentConfig
from user.decorators import student_required

app_name = StudentConfig.name

urlpatterns = [
    path("dashboard/", student_required(DashboardView.as_view()), name="dashboard"),
]
