from django.urls import path
from .views import createViolate
from .apps import ViolationConfig

app_name = ViolationConfig.name

urlpatterns = [
    path("ajax/createViolation/", createViolate, name="violate"),
]
