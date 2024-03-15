from django.contrib import admin
from django.urls import path, include
from users.views import role_based_redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('role_based_redirect/', role_based_redirect, name='role_based_redirect'),
    path('', include('users.urls')),  # Include users.urls at the root.
    path('users/', include('django.contrib.auth.urls')),  # Utilizes Django's built-in auth views.
    path('users/', include('users.urls')),  # Custom user app URLs.
    path('courses/', include('courses.urls')),  # Custom courses app URLs.
    # Add other paths as needed.
]
