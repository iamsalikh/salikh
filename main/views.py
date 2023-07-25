from django.shortcuts import render, redirect
from .models import Course
from .forms import TaskForm


def index(request):
    tasks = Course.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def register(request):
    return render(request, 'main/register.html')


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)