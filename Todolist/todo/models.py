from django.db import models

class ListWork(models.Model):
    title = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    urgency = models.FloatField(default=0.5)
    importance = models.FloatField(default=0.5)
    priority = models.IntegerField(default=0) 

    def __str__(self):
        return self.title
