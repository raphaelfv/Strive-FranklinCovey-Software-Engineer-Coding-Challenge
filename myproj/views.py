from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import *
from .models import *
from django.contrib import messages
from django.views.generic.list import ListView

def first(request):
    return render(request, 'first.html', {})

class AnsweredListView(ListView):

    model = QuizAnswer
    template_name="answered.html"

    def get_queryset(self):
        return self.model.objects.filter(question__id=1) # TODO - get from kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class NewAnswerView(View):
    form_class = QuizAnswerForm
    template_name = 'answer.html'

    def get(self, request, *args, **kwargs):
        step = kwargs.get('step')
        question_id = kwargs.get('question_id')
        print("=============step,",step)
        form = self.form_class()
        question = QuizQuestion.objects.get(id=question_id)
        return render(request, self.template_name, {'form': form, 'question':question})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            messages.success(request,'Question inserted on the database')
            return HttpResponseRedirect('')

        return render(request, self.template_name, {'form': form})
