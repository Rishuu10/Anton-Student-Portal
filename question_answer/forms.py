from .models import Question, Answer, Option, ActiveQuestion


class QuestionCreateForm:
    def createQuestion(self, text, teacher):
        instance = Question(text=text, teacher=teacher)
        instance.save()
        return instance.id


class ActiveQuestionCreateForm:
    def createActiveQuestion(self, question_id):
        question_instance = Question(pk=question_id)
        instance = ActiveQuestion(question=question_instance)
        instance.save()
        return instance.id


class AnswerCreateForm:
    def createAnswer(self, option_id, student):
        opt_instance = Option.objects.filter(id=option_id)[0]
        question = opt_instance.question
        active_question = ActiveQuestion.objects.filter(question=question)[0]
        instance = Answer(option=opt_instance, student=student,
                          active_question=active_question)
        instance.save()
        return instance.id


class OptionCreateForm:
    def createOption(self, text, question_id):
        question_instance = Question(pk=question_id)
        instance = Option(question=question_instance, text=text)
        instance.save()
        return instance.id
