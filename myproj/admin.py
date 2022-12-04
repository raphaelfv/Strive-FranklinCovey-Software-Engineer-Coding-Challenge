from django.contrib import admin
from .utils import PrintException
from django.contrib.auth.models import User

# Register your models here.
from myproj.models import *
try:
    admin.site.register(QuizCollection)
    admin.site.register(QuizAnswer)
    admin.site.register(QuizQuestion)
except Exception as ex:
    print ("[admin] Error including model on /admin",ex)

try:
    if not QuizCollection.objects.all().exists():
        user = User.objects.first()
        collection = QuizCollection.objects.create(author=user)

        QuizQuestion.objects.create(question="What is your favorite colour?", collection=collection)
        QuizQuestion.objects.create(question="What is your favorite fruit?", collection=collection)
        QuizQuestion.objects.create(question="What is your favorite song?", collection=collection)
        QuizQuestion.objects.create(question="When is your birthday?", collection=collection)
        QuizQuestion.objects.create(question="What is your telephone number?", collection=collection)
except Exception as ex:
    PrintException()
