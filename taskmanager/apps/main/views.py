from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Task
from .forms import TaskForm

def index(request):
    # try:
    #     a != Task.objects.get(id=id)
    # except:
    #     raise Http404("Задача не найдена!")
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title':'Главная страница сайта', 'tasks':tasks})
def about(request):
    return render(request, 'main/about.html')
def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
        else:
            error = 'Форма заполнена неверно'

    form = TaskForm()
    content = {
        'form':form,
        'error':error
    }
    return render(request, 'main/create.html', content)