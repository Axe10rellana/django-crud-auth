# importaciones
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.utils import timezone
from .models import Task
from .forms import TaskForm
import datetime as dt

# Create your views here.


def home(request):
    userName = 'Axe10rellana'
    currentDateTime = dt.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    appName = 'Django Crud Auth'
    return render(request, 'home.html', {
        'userName': userName,
        'year': year,
        'appName': appName
    })


def signup(request):
    userName = 'Axe10rellana'
    currentDateTime = dt.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    appName = 'Django Crud Auth'

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'userName': userName,
            'year': year,
            'appName': appName,
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'userName': userName,
                    'year': year,
                    'appName': appName,
                    'form': UserCreationForm,
                    'error': "El usuario ya existe"
                })
        return render(request, 'signup.html', {
            'userName': userName,
            'year': year,
            'appName': appName,
            'form': UserCreationForm,
            'error': "Las contraseñas no coinciden"
        })


@login_required
def tasks(request):
    userName = 'Axe10rellana'
    currentDateTime = dt.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    appName = 'Django Crud Auth'
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {
        'userName': userName,
        'year': year,
        'appName': appName,
        'tasks': tasks
    })


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    userName = 'Axe10rellana'
    currentDateTime = dt.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    appName = 'Django Crud Auth'

    if request.method == 'GET':
        return render(request, 'signin.html', {
            'userName': userName,
            'year': year,
            'appName': appName,
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'userName': userName,
                'year': year,
                'appName': appName,
                'form': AuthenticationForm,
                'error': "El nombre de usuario o la contraseña es incorrecto"
            })
        else:
            login(request, user)
            return redirect('tasks')


@login_required
def create_task(request):
    userName = 'Axe10rellana'
    currentDateTime = dt.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    appName = 'Django Crud Auth'

    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'userName': userName,
            'year': year,
            'appName': appName,
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
                'userName': userName,
                'year': year,
                'appName': appName,
                'form': TaskForm,
                'error': "Porfavor complete el formulario con datos validos"
            })


@login_required
def task_detail(request, task_id):
    userName = 'Axe10rellana'
    currentDateTime = dt.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    appName = 'Django Crud Auth'
    task = get_object_or_404(Task, pk=task_id, user=request.user)

    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {
            'userName': userName,
            'year': year,
            'appName': appName,
            'task': task,
            'form': form
        })
    else:
        try:
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks_completed')
        except ValueError:
            return render(request, 'task_detail.html', {
                'userName': userName,
                'year': year,
                'appName': appName,
                'task': task,
                'form': form,
                'error': "Error Actualizando La Tarea"
            })


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks_completed')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks_completed')


@login_required
def tasks_completed(request):
    userName = 'Axe10rellana'
    currentDateTime = dt.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    appName = 'Django Crud Auth'
    tasks = Task.objects.filter(
        user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    tasksCompleted = True

    return render(request, 'tasks.html', {
        'userName': userName,
        'year': year,
        'appName': appName,
        'tasks': tasks,
        'tasksCompleted': tasksCompleted
    })
