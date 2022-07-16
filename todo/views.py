import string
from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    # return HttpResponse("Here MainPage")
    # context = {
    #   "numbers" : [10,20,30,40,50],
    # }
    return render(request, "index.html",{
        "todos": todos,
    })
def addTodo(request):
    if request.method == "GET":
            return redirect("/")
    else:
        title = request.POST.get("todotitle")
        newTodo = Todo(title = title,completed = False)
        newTodo.save()
        return redirect("/")
def updateTodo(request,id):
    # todo = Todo.objects.filter(id = id).first()
    todo = get_object_or_404(Todo,id = id)

    todo.completed = not todo.completed
    todo.save()
    return redirect("/")
def deleteTodo(request,id):
    todo = get_object_or_404(Todo,id=id)
    todo.delete()
    return redirect("/")

