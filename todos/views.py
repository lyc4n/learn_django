from django.shortcuts import render, redirect
from django.http import HttpResponse
from todos.models import Todo
from django.utils.timezone import datetime
from IPython import embed

def index(request):
    todos = Todo.objects.filter(due_date__date=datetime.today())
    context = {'todos': todos}
    return render(request, 'index.html', context)

def finish(request, id):
    todo = _get_todo(id)
    todo.update(is_done=True)
    return redirect('todos_index')

def unfinish(request, id):
    todo = _get_todo(id)
    todo.update(is_done=False)
    return redirect('todos_index')

def _get_todo(id):
    todo = Todo.objects.filter(id=id)
    return todo
