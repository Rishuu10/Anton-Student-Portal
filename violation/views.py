from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .forms import ViolationForm
User = get_user_model()


def createViolate(request):
    text = request.GET.get('text', 'Question not added')
    user = request.user
    instance = ViolationForm()
    instance.createViolation(text=text, student=user)
    data = {
        'is_addded': True,
    }
    return JsonResponse(data)
