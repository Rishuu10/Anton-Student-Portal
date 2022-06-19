from django.shortcuts import render
from django.views import View
from question_answer.models import ActiveQuestion, Answer
from teacher.models import TimeTable

# Create your views here.


class DashboardView(View):
    template_name = "student/dashboard.html"

    def get(self, request):
        answer_objs = Answer.objects.filter(student=request.user)
        active_qs = ActiveQuestion.objects.exclude(
            question__id__in=[answer.active_question.question.id for answer in answer_objs])
        if len(active_qs):
            active_qs = active_qs[0]
        else:
            active_qs = []
        tt = TimeTable.objects.all()
        tot_ans = len(answer_objs)
        tot_qs = len(ActiveQuestion.objects.all())
        return render(request, self.template_name, {'active_qs': active_qs, 'student': request.user, 'tt': tt, 'tot_ans': tot_ans, 'tot_qs': tot_qs})
