from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True) 

   
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups", 
        blank=True,
        verbose_name="groups",
        help_text="The groups this user belongs to.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions", 
        blank=True,
        verbose_name="user permissions",
        help_text="Specific permissions for this user.",
    )

    def __str__(self):
        return self.username

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name