from django.shortcuts import redirect, render
from .models import Home
# Create your views here.

def index(request):
    tasks = Home.objects.all()
    return render(request, 'home/index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Home.objects.create(title=title, description=description)
        return redirect('index')   
    return render(request, 'home/add_task.html')

def complete_task(request, task_id):
    task = Home.objects.get(id=task_id)
    task.completed = True
    task.status = 'completed'
    task.save()
    return redirect('index')

def delete_task(request,task_id):
    task = Home.objects.get(id=task_id)
    task.delete()
    return redirect('index')

def update_task(request, task_id):
    task = Home.objects.get(id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('index')
    return render(request, 'home/update_task.html', {'task': task})
