from .models import Violation

class ViolationForm:
    def createViolation(self, text,student):
        instance = Violation(text = text, student = student)
        instance.save()
        return instance.id