from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import CustomUser 
from .forms import UserRegisterForm 

def homepage(request):
    return render(request, 'homepage.html')

def student_dashboard(request):
    return render(request, 'users/student_dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user immediately after registration
            return redirect('role_based_redirect')  # Redirect based on the user's role
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def role_based_redirect(request):
    role = request.user.role
    if role == CustomUser.ADMIN:
        return redirect('admin_dashboard')
    elif role == CustomUser.INSTRUCTOR:
        return redirect('instructor_dashboard')
    elif role == CustomUser.STUDENT:
        return redirect('student_dashboard')
    else:
        # Handle undefined or invalid roles
        return redirect('homepage')  # Redirect to homepage or display an error message

@login_required
def student_dashboard(request):
    if request.user.role != CustomUser.STUDENT:
        return redirect('role_based_redirect')
    return render(request, 'dashboard/student_dashboard.html')

@login_required
def instructor_dashboard(request):
    if request.user.role != CustomUser.INSTRUCTOR:
        return redirect('role_based_redirect')
    return render(request, 'dashboard/instructor_dashboard.html')

@login_required
def admin_dashboard(request):
    if request.user.role != CustomUser.ADMIN:
        return redirect('role_based_redirect')
    return render(request, 'dashboard/admin_dashboard.html')
