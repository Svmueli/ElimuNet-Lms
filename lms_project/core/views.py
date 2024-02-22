
# Create your views here.

from django.shortcuts import render

def signup_view(request):
    """Render signup page."""
    return render(request, 'signup.html')

def login_view(request):
    """Render login page."""
    return render(request, 'login.html')

def course_creation_view(request):
    """Render course creation page."""
    return render(request, 'course_creation.html')

def assignment_creation_view(request):
    """Render assignment creation page."""
    return render(request, 'assignment_creation.html')

def user_profile_view(request):
    """Render user profile page."""
    return render(request, 'user_profile.html')
