from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import *
from django.shortcuts import render, redirect,HttpResponse
from .forms import StudentIDLoginForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
@login_required
def home(request):
    return render(request,'home.html')


def login_view(request):
    if request.method == 'POST':
        form = StudentIDLoginForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data.get('student_id')
            password = form.cleaned_data.get('password')
            user = authenticate(request, student_id=student_id, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid student ID or password")
    else:
        form = StudentIDLoginForm()
    
    return render(request, 'intial_login.html', {'forms': form})
@login_required
def register(request):
    user = request.user  

    if request.method == 'POST':
        form = PasswordSetupForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password1')
            user.set_password(password)  
            user.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Password set successfully.')
            return HttpResponse('success')  
    else:
        form = PasswordSetupForm()


    context = {
        'form': form,
        'user_details': {
            'student_id': user.student_id,
            'name': user.name,
            'branch': user.branch,
            'batch': user.Batch,
            
        }
    }
    
    return render(request, 'register.html', context)
@login_required
def student_login_view(request):
    if request.method == 'POST':
        form = StudentIDLoginForm1(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data.get('student_id')
            user = authenticate(request, student_id=student_id)
            if user is not None:
                login(request, user)
                return redirect('register')  
    else:
        form = StudentIDLoginForm1()
    return render(request, 'login.html', {'form': form})
