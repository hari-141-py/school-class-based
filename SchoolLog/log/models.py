from django.db import models

class School(models.Model):
    name=models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    population = models.IntegerField()
    faculty = models.IntegerField()
    details = models.CharField(max_length=30)

    def __str__(self):
        return self.name