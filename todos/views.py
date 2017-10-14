from django.shortcuts import render, redirect
from django.http import HttpResponse
from todos.models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from IPython import embed

@login_required
def index(request):
    unfinished = _todos_today(request.user).filter(is_done=False)
    finished   = _todos_today(request.user).filter(is_done=True)
    context    = {'unfinished_todos': unfinished, 'finished_todos': finished}
    return render(request, 'index.html', context)

@login_required
def finish(request, id):
    todo = _get_todo(request.user, id)
    todo.update(is_done=True)
    return redirect('todos_index')

@login_required
def unfinish(request, id):
    todo = _get_todo(request.user, id)
    todo.update(is_done=False)
    return redirect('todos_index')

@login_required
def create(request):
    todo = Todo(title=request.POST['title'],
                description=request.POST['description'],
                due_date=timezone.now().date(),
                user_id=request.user.id)
    todo.save()
    return redirect('todos_index')

@login_required
def destroy(request, id):
    todo = _get_todo(request.user, id)
    todo.delete()
    return redirect('todos_index')

def _get_todo(user, id):
    todo = Todo.objects.filter(id=id, user_id=user.id)
    return todo

def _todos_today(user):
    todos = Todo.objects.filter(user=user, due_date__date=timezone.datetime.today())
    return todos
