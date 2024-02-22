
from django.urls import path
from .views import signup_view, login_view, course_creation_view, assignment_creation_view, user_profile_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('course_creation/', course_creation_view, name='course_creation'),
    path('assignment_creation/', assignment_creation_view, name='assignment_creation'),
    path('user_profile/', user_profile_view, name='user_profile'),
    
    # Add more URL patterns as needed
]
