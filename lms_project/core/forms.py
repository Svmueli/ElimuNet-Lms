from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Course, Assignment

class SignupForm(UserCreationForm):
    # You can customize fields here if needed
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    # You can customize fields here if needed
    class Meta:
        model = User
        fields = ['username', 'password']

class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'teacher']

class AssignmentCreationForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'course']
