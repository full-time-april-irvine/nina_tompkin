from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email_address = models.CharField(max_length=225)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Users: {self.first_name} {self.last_name}, {self.email_address}, {self.age}"