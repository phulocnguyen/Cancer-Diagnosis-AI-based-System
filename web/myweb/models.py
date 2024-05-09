from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    full_name = models.CharField(max_length=200, null=True) 

    def __str__(self):
        return self.full_name if self.full_name else str(self.user)
