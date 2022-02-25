from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    salary = models.IntegerField()
    date_of_birth = models.DateTimeField()

    def __str__(self):
        return self.name

