from django.shortcuts import render

# Create your views here.
def AddTasks(request):
    context = {'task': 'read a book'}
    return render(request, 'checklist/main.html', context)