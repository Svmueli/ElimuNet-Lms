
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('create-course/', views.course_creation_view, name='create_course'),
    path('create-assignment/', views.assignment_creation_view, name='create_assignment'),
    path('profile/', views.user_profile_view, name='user_profile'),
    
    # Add more URL patterns as needed
]
