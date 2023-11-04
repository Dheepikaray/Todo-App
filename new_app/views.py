from django.shortcuts import render, redirect

from new_app.forms import TodoForm
from new_app.models import Todo


def new(request):
    return render(request, 'index.html')


# Create your views here.

def create(request):
    form = TodoForm()
    if request.method == "POST":
        form1 = TodoForm(request.POST)
        if form1.is_valid():
            form1.save()
        else:
            form=form1
    return render(request, "add.html", {"form": form})


# read data

def view(request):
    data = Todo.objects.all()
    return render(request, "view.html", {"data": data})



# delete

def delete(request,id):
    if request.method == 'POST':

        delt = Todo.objects.get(id=id)
        delt.delete()

        return redirect("view")
    return render(request,"corona.html")

# update

def update(request,id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form1 = TodoForm(request.POST,instance=todo)
        if form1.is_valid():
            form1.save()
            return redirect("view")
        else:
            form=form1
    return render(request,'update.html',{'form':form})
