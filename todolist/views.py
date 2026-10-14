from django.shortcuts import redirect, render
from .models import Task

def task_list(request):
    todo_list = Task.objects.order_by('-created_at')
    return render(request, 'todolist/index.html', {"todo_list": todo_list})
    
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
    return redirect('todolist:index')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('todolist:index')

def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('todolist:index')


