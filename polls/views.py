from django.shortcuts import render


def index(request):
    polls = ["First poll", "Second poll", "Third poll"]
    return render(request, 'polls.html', {'polls': polls})