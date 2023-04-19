from django.shortcuts import render, redirect
from crudApp.forms import StudentForm
from crudApp.models import Student


def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StudentForm()
        return render(request, 'index.html', {'form': form})


def show(request):
    students = Student.objects.all().values()
    return render(request, 'show.html', {'students': students})


def edit(request, id):
    students = Student.objects.get(id=id)
    return render(request, 'edit.html', {'student': students})


def delete(request, id):
    students = Student.objects.get(id=id)
    students.delete()
    return redirect('/show')


def update(request, id):
    students = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=students)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'student': students})
