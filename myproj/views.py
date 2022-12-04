from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
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
    step = 1
    collection_id = 1

    def getQuestion(self,collection_id,step):
        questionQS = QuizQuestion.objects.filter(collection__id=collection_id)
        questionIDs = list(questionQS.values_list('id',flat=True))
        questionID = questionIDs[step-1]
        question = QuizQuestion.objects.get(id=questionID)
        return question
        
    def get(self, request, *args, **kwargs):
        self.step = kwargs.get('step')
        self.collection_id = kwargs.get('collection_id')
        print('=============self.collection_id,',self.collection_id)
        question = self.getQuestion(collection_id=self.collection_id ,step=self.step)
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'question':question})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        step = kwargs.get('step')
        collection_id = kwargs.get('collection_id')
        if form.is_valid():
            newObj = form.save(commit=False)
            question = self.getQuestion(collection_id=collection_id,step=step)
            newObj.question = question
            try:
                newObj.answered_by = self.request.user 
            except:
                newObj.answered_by = User.objects.first() # TODO: ensure user is logged in
            newObj.save()
            if step != 5:
                messages.success(request,'Answer inserted on the database')
                return redirect('answer', step=step+1, collection_id=collection_id)
            else:
                messages.success(request,'Quiz completed with success')
                return redirect('first')

        return render(request, self.template_name, {'form': form})
