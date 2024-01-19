from django.db import models

# Create your models here.


class Passengers(models.Model):
    id = models.AutoField(primary_key=True)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Travel_point = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.id+self.Firstname+self.Lastname+self.Travel_point