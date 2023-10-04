from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import *
def index(request):
    if request.method == 'POST':
        ToDo.objects.create(
            title=request.POST.get('name'),
            date=request.POST.get('date'),
            status=request.POST.get('status'),
            detail=request.POST.get('details'),
            owner=request.user,
        )
        return redirect('/index/')
    if request.user.is_authenticated:
       content = {
         'todos': ToDo.objects.filter(owner=request.user)
       }
       return render(request, 'index.html', content)
    return redirect('/')
def edit(request, pk):
    if request.method == 'POST':
        ToDo.objects.filter(id=pk).update(
            status=request.POST.get('status')
        )
        return redirect('/index/')
    content = {
        'todo': ToDo.objects.get(id=pk)
    }
    return render(request, 'edit.html', content)
def delete_todo(request, pk):
    ToDo.objects.get(id=pk).delete()
    return redirect('/index/')
def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST.get('login'),
            password = request.POST.get('parol')
        ) # -> None, yoki userni return qiladi
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/index/')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

