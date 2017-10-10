from django.shortcuts import render, redirect
from django.http import HttpResponse
from todos.models import Todo
from django.utils.timezone import datetime
from IPython import embed

def index(request):
    todos = Todo.objects.filter(due_date__date=datetime.today())
    context = {'todos': todos}
    return render(request, 'index.html', context)

def finish(request, todo_id):
    todo         = Todo.objects.filter(id=todo_id).first()
    todo.is_done = True
    todo.save()
    return redirect('todos_index')

def unfinish(request, todo_id):
    todo         = Todo.objects.filter(id=todo_id).first()
    todo.is_done = False
    todo.save()
    return redirect('todos_index')
