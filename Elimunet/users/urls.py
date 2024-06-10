from django.urls import path
from . import views

urlpatterns = [
    # Existing user-related paths
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/instructor/', views.instructor_dashboard, name='instructor_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('logout/', views.logout, name='logout'),


    
]
