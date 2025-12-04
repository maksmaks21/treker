from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    STATUS_CHOICES = [
    ('todo', 'To Do'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    ]
    PRIORITY_CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
    ]

    title = models.CharField(max_length=200, verbose_name="Task Title")
    description = models.TextField(verbose_name="Task Description", blank=True, null=True)
    dedline = models.DateTimeField(verbose_name="Deadline", blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='todo', verbose_name="Task Status")
    priority= models.CharField(choices=PRIORITY_CHOICES, max_length=20, default='low', verbose_name="Task Priority")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_ad=models.DateTimeField(auto_now_add= True)
    update_ad=models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title
    

class Comennt(models.Model):
    content=models.TextField(verbose_name='Comennt')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task=models.ForeignKey(Task, on_delete=models.CASCADE)
    media=models.FileField(upload_to='comennt_media', blank=True, null=True)
    create_ad=models.DateTimeField(auto_now_add= True)