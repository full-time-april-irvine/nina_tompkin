from django.db import models
from datetime import datetime, date
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    
    
    def validate(self, form):
        errors = []

        if len(form["first_name"]) < 2:
            errors.append("First name should be at least 2 characters.")
        if len(form["last_name"]) < 2:
            errors.append("Last name should be at least 2 characters.")
        if not EMAIL_REGEX.match(form["email"]):
            errors.append("Email must be in a valid format.")
        matching_users = Users.objects.filter(email=form["email"])
        if matching_users:
            errors.append("Email already in use")
        if not form["birthday"]:
            errors.append("Please enter your birthday.")
        else:
            entered_date = datetime.strptime(form["birthday"], '%Y-%m-%d')
            if entered_date > datetime.now():
                errors.append("Birthday must be in the past.")
        if len(form["password"]) < 8:
            errors.append("Password should be at least 8 characters.")
        if form["password"] != form["password2"]:
            errors.append("Passwords do not match.")
        print("*"*50)
        print(form)
        print("*"*50)
        return errors

    def easy_create(self, form):
        pw_hash = bcrypt.hashpw(form["password"].encode(), bcrypt.gensalt())

        user = Users.objects.create(
            first_name=form["first_name"],
            last_name=form["last_name"],
            email=form["email"],
            birthday=form["birthday"],
            pw_hash=pw_hash
        )
        return user

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    pw_hash = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()