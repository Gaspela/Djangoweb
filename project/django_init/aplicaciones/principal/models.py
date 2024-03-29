from django.db import models
# Representacion de las tablas de la  base de datos
# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    cc = models.PositiveBigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=200)


def __str__(self):
    return self.name
