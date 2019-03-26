from django.db import models

# Create your models here.
class workout(models.Model):
    pushups = models.IntegerField()
    situps = models.IntegerField()
    name = models.CharField(max_length=1024)
    date = models.CharField(max_length=1024)
    #makes Workout table with these

    def __str__(self):
        return self.email