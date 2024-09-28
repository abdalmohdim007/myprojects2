from django.db import models
from django.contrib.auth.models import User

class Function(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Template(models.Model):
    name = models.CharField(max_length=255)
    project_name = models.TextField()
    brief = models.TextField()
    description = models.TextField()
    

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)  # Required field
    description = models.TextField()  # Required field
    apps = models.ManyToManyField('App')  # Multiple select for apps
    functions = models.ManyToManyField(Function)  # Multiple select for functions
    templates = models.ManyToManyField(Template)  # Multiple select for templates
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class App(models.Model):
    app_name = models.CharField(max_length=255)  # App name model for multiple select

    def __str__(self):
        return self.app_name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    name = models.CharField(max_length=255)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)  # The user assigned to the task
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')])

    def __str__(self):
        return f"{self.name} - {self.status} for {self.project.name}"


class Contact(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  message = models.TextField()