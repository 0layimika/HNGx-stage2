from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=60,default='')
    dob = models.CharField(max_length=12,default='')
    address = models.CharField(max_length=60,default='')
    telephone = models.CharField(max_length=14,default='')

    def __str__(self):
        return self.name