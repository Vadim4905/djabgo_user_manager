from django.db import models

# Create your models here.

class User(models.Model):
    class Role(models.TextChoices):
        admin='admin', 'ADMIN'
        user = 'user', 'USER'
    name =  models.CharField(max_length=100,unique=True)
    email = models.EmailField()
    role = models.CharField(max_length=100,choices=Role.choices,default=Role.user)

    def __str__(self):
        return self.name


