# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

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

    #can/will add additional fields if needed

class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Add additional fields specific to admin, if any

class Instructor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Add additional fields specific to instructor, if any

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Add additional fields specific to student, if any