from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    gender = models.TextField(null=True)
    age = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    email = models.TextField(null=True)
