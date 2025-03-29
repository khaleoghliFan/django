from django.shortcuts import render, redirect
from .models import ListWork
from django.contrib import messages


def perceptron(inputs, weights):
    total = sum(i * w for i, w in zip(inputs, weights))
    return 1 if total > 0.5 else 0  # شرط اولویت

def todo_list(request):
    todos = ListWork.objects.all()  # دریافت تمام وظایف
    weights = [0.5, 0.5]  # وزن‌های نمونه برای فوریت و اهمیت

    if request.method == 'POST':
        title = request.POST.get('title')
        urgency = float(request.POST.get('urgency', 0.5))
        importance = float(request.POST.get('importance', 0.5))
        new_todo = ListWork(title=title, urgency=urgency, importance=importance)
        new_todo.save()

    for todo in todos:
        inputs = [todo.urgency, todo.importance]
        todo.priority = perceptron(inputs, weights)
        todo.save()

    todos = ListWork.objects.all().order_by('-priority')  # مرتب‌سازی بر اساس اولویت

    return render(request, 'todo_list.html', {'todos': todos})



def task_delete(request, task_id):
    task = ListWork.objects.get(id=task_id)
    task.delete()
    messages.success(request, 'وظیفه با موفقیت حذف شد.')

    return redirect('todo_list')



def task_complete(request, task_id):
    task = ListWork.objects.get(id=task_id)
    task.completed = True
    task.save()
    messages.success(request, 'وظیفه با موفقیت تکمیل شد.')

    return redirect('todo_list')
