from django.db import models
from datetime import datetime as dt

# Create your models here.

class Task(models.Model):
    # An ID field is automatically added to all Django models
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

class Note(models.Model):
    # An ID field is automatically added to all Django models
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text
        
   
