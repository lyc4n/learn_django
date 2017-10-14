from django.shortcuts import render, redirect
from django.http import HttpResponse
from todos.models import Todo
from django.utils import timezone
from IPython import embed

def index(request):
    unfinished = _todos_today().filter(is_done=False)
    finished   = _todos_today().filter(is_done=True)
    context    = {'unfinished_todos': unfinished, 'finished_todos': finished}
    return render(request, 'index.html', context)

def finish(request, id):
    todo = _get_todo(id)
    todo.update(is_done=True)
    return redirect('todos_index')

def unfinish(request, id):
    todo = _get_todo(id)
    todo.update(is_done=False)
    return redirect('todos_index')

def create(request):
    todo = Todo(title=request.POST['title'],
                description=request.POST['description'],
                due_date=timezone.now().date())
    todo.save()
    return redirect('todos_index')

def destroy(request, id):
    todo = _get_todo(id)
    todo.delete()
    return redirect('todos_index')

def _get_todo(id):
    todo = Todo.objects.filter(id=id)
    return todo

def _todos_today():
    todos = Todo.objects.filter(due_date__date=timezone.datetime.today())
    return todos
