from django.shortcuts import render
from django.views import View
from question_answer.models import Question, ActiveQuestion
from violation.models import Violation
# Create your views here.


class DashboardView(View):
    template_name = "teacher/dashboard.html"

    def get(self, request):
        questions = Question.objects.all()
        active_questions = ActiveQuestion.objects.all()
        tot_violations = Violation.objects.all()
        dict = {}
        for viol in tot_violations:
            dict[f"{viol.student.pk}"] = dict.get(f"{viol.student.pk}", 0) + 1
        print(dict)
        return render(request, self.template_name, {'teacher':request.user,'questions': questions, 'active': active_questions, 'violations': dict})
