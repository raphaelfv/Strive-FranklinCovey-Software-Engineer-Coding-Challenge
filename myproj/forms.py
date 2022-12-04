from django.forms import ModelForm
from .models import QuizAnswer

class QuizAnswerForm(ModelForm):
     class Meta:
         model = QuizAnswer
         fields = ['answer']
