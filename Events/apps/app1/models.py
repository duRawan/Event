from django.db import models




class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["first_name"]) < 1:
            errors["first_name"] = "User first name should be at least 1 characters"
        if len(postData["last_name"]) < 1:
            errors["last_name"] = "User last name should be at least 1 characters"
        if len(postData["email"]) < 1:
            errors["email"] = "User email should be at least 1 characters"
        if len(postData["password"]) < 8:
            errors["password"] = "User password should be at least 8 characters"
        return errors

class Event(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    numberOfTickets = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    first_name= models.CharField(max_length=45)
    last_name= models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    events=models.ForeignKey(Event,related_name="users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
