from django.db import models

# Create your models here.

class User(models.Model):
    ceilphone = models.CharField(max_length=11)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    salts=models.CharField(max_length=5)
    user_status=models.BooleanField()
    class Meta:
        db_table = 't_user'