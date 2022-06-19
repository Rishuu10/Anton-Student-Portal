from django.contrib import admin
from .models import Question, Answer, Option, ActiveQuestion
# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Option)
admin.site.register(ActiveQuestion)
