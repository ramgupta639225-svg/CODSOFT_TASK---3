from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    phone = models.CharField(unique=True, max_length=13)
    address = models.TextField()
    membership_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

