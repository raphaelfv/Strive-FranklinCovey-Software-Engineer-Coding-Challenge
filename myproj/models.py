from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class QuizCollection(models.Model):
    insertion_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Insertion Date"))
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = True
    
class QuizQuestion(models.Model):
    question = models.CharField(max_length=100, verbose_name=_("Question"), help_text=_('Example: What country is inside South Africa?'))
    collection = models.ForeignKey(QuizCollection, on_delete=models.CASCADE)

    class Meta:
        managed = True

class QuizAnswer(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Insertion Date"))
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_answer')
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100, verbose_name=_("Answer"), help_text=_('Fill with your answer'), blank=True, null=True)

    class Meta:
        managed = True