from django.shortcuts import render
from polls.models import Question

def index(request):
    questions = Question.objects.all()
    print(questions)
    return render(request, 'polls.html', {'questions': questions})