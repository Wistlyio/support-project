from django.db import models

# Create your models here.
#class Student(models.Model):
    # id = models.AutoField(primary_key=True, unique=True)
    # first_name = models.TextField(null=True)
    # last_name = models.TextField(null=True)
    # gender = models.TextField(null=True)
    # age = models.IntegerField(null=True)
    # date_created = models.DateTimeField(auto_now_add=True)
    # email = models.TextField(null=True)

    # def __str__(self):
    #   return "{}".format(self)

# If they're not logged in
class Ticket(models.Model) :
    id = models.AutoField(primary_key = True, unique = True)
    first_name = models.TextField(null = True)
    last_name = models.TextField(null = True)
    date_created = models.DateTimeField(auto_now_add=True)
    email = models.TextField(null = True)
    issue_summary = models.TextField(null = True)
    extra_details = models.TextField(null = True)

    def __str__(self) :
        return "{}".format(self)

class Agent(models.Model) :
    id = models.AutoField(primary_key = True, unique = True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()

    def __str__(self) :
        return "{}".format(self)

# # If they're logged in
# class Ticket2(models.Model) :
#     id = models.AutoField(primary_key = True, unique = True)
#     user_id = models.TextField(null = True)
#     date_created = models.DateTimeField(auto_now_add= True)
#     issue_summary = models.TextField(null = True)
#     extra_details = models.TextField(null = True)