from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=200)
    state = models.CharField(max_length=15, choices=(('completed', 'Completed'), ('in progress', 'In Progress'), ('planned', 'Planned')))

    def __str__(self):
        return self.task