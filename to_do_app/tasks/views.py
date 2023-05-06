from django.shortcuts import render, redirect

# Create your views here.
from .models import Task
from .forms import taskForm


def index(request):

    tasks = Task.objects.all()

    form = taskForm()
   
    if request.method == "POST":
        form = taskForm(request.POST, request.FILES)

        if form.is_valid():
           form.save()
           return redirect('list')
    
   

    return render(request, 'tasks/index.html', {'tasks': tasks, 'form':form})


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = taskForm(instance=task)

    if request.method == "POST":
        form = taskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list')
    

    return render(request, 'tasks/update_task.html',{
        'form': form,
    })

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('list')
    return render(request, 'tasks/delete.html',{'task':task})