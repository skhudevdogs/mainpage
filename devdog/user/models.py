from django.db import models

# Create your models here.
class User(models.Model):
    student_id = models.CharField(max_length=9)
    name = models.CharField(max_length=4)
    password = models.CharField(max_length=12)