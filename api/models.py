from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=50)
    dep_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.full_name

