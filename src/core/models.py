from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=20, editable=False, unique=False, blank=False, null=False)
    age = models.IntegerField(unique=False, editable=True, blank=False, null=False)
    cellphone = models.CharField(max_length=11, editable=True, unique=True, blank=False, null=False)
    position = models.CharField(max_length=10, editable=True, unique=False, blank=False, null=True)
    salary = models.FloatField(editable=True, unique=False, null=True, blank=False)

    def __str__(self):
        return f"{self.name}"