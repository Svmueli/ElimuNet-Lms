from django.shortcuts import render, redirect
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm
from .models import CustomUser, Admin, Instructor, Student

def role_based_redirect(request):
    user = request.user
    if user.is_authenticated:
        if user.role == CustomUser.STUDENT:
            return redirect('student_dashboard')
        elif user.role == CustomUser.INSTRUCTOR:
            return redirect('instructor_dashboard')
        elif user.role == CustomUser.ADMIN:
            return redirect('admin_dashboard')
    return redirect('homepage')

def homepage(request):
    return render(request, 'homepage.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.role == CustomUser.STUDENT:
                Student.objects.create(user=user)
            elif user.role == CustomUser.INSTRUCTOR:
                Instructor.objects.create(user=user)
            elif user.role == CustomUser.ADMIN:
                Admin.objects.create(user=user)
            return redirect('role_based_redirect')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

@login_required
def instructor_dashboard(request):
    return render(request, 'instructor_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_update')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'profile_update.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('homepage')
