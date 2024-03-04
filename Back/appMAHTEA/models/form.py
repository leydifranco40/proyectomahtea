from django.db import models
from .user import User

class Form(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    phone = models.BigIntegerField(default = 0)
    birthdate= models.DateField()
    adress = models.CharField(max_length =30)
    occupation = models.CharField(max_length = 50)
    gender = models.CharField(max_length =30)
    city = models.CharField(max_length =30)
    