from django.shortcuts import render
from .models import Todo
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def todo_list(request):  #  함수형
    todos = Todo.objects.all()
    return render(request, "todo/todo.html", {"todos": todos})
