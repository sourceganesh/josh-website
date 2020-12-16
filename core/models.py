from django.db import models

# Create your models here.
class EventsList(models.Model):
    name          = models.CharField(max_length=50)
    date          = models.DateField()
    participants  = models.IntegerField()

    def __str__(self):
        return self.name + " " + str(self.date)