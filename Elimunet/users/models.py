from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    # Define user roles
    ADMIN = 1
    INSTRUCTOR = 2
    STUDENT = 3
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (INSTRUCTOR, 'Instructor'),
        (STUDENT, 'Student'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Add additional fields specific to admin, if any

class Instructor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Add additional fields specific to instructor, if any

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    admission_number = models.CharField(max_length=20, default='')  # Default to empty string
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    class_name = models.CharField(max_length=100, default='Unknown Class')  # Default to 'Unknown Class'
    course = models.CharField(max_length=100, default='Unknown Course')  # Default to 'Unknown Course'
