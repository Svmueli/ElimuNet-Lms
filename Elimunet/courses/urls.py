from django.urls import path
from . import views

app_name = 'courses'  # Define the application name to use as namespace

urlpatterns = [
    path('', views.index, name='index'),  # The 'index' name corresponds to '{% url 'courses:index' %}'
]
