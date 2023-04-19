from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Task
from .forms import TaskForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        form = TaskForm()
        tasks = Task.objects.filter(account=request.user.account).order_by('task_priority')
        if len(tasks) > 0:
            avail = True
        else:
            avail = False

        context = {'form': form, 'tasks': tasks, 'avail': avail}
        return render(request, 'tasktracker/task.html', context)
    else:
        return redirect('login')

def add_task(request):
    # If the user is authenticated and has posted a task
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()

            # Getting the last saved task
            saved_form = Task.objects.latest('created')
            saved_form.account = request.user.account
            saved_form.save()

            return redirect("home")

def delete_task(request, pk):
    try:
        task_to_delete = Task.objects.get(pk=pk)
        task_to_delete.delete()

        return redirect('home')
    except:
        pass

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            # If user does not exist
            return redirect('signin')

        # If user exists log them in
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'tasktracker/login.html')

def signin_user(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('home')

    context = {'form':form}
    return render(request, 'tasktracker/signin.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')