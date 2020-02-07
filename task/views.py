from django.shortcuts import render
from django import forms
from task.forms import *
from task.models import *


# Create your views here. 

def create_task(request):
    if request.method=="POST":
        task_title = request.POST.get("task")
        description = request.POST.get("desc")
        end_date = request.POST.get("date")
        status = request.POST.get("status")


        t = Task.objects.get_or_create(task_title = task_title,description = description,end_date=end_date,status=status)[0]
        t.save()
    return render(request,'create_task.html')

def display_task(request):
    tasks = Task.objects.all()    
    return render(request, 'display_task.html', context={'tasks':tasks})

def comment(request):
    tasks = Task.objects.all()
    return render(request, 'comment.html', context={'tasks':tasks})




























