from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Question(models.Model):
    text = models.CharField(max_length=500)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text


class ActiveQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "Active Question"


class Option(models.Model):
    text = models.CharField(max_length=600)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")

    def __str__(self) -> str:
        return self.text


class Answer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    active_question = models.ForeignKey(ActiveQuestion, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Answer"
