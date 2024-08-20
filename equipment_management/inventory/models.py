from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields can be added here if necessary

    def __str__(self):
        return self.user.username

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    issued_date = models.DateField(null=True, blank=True)  # New field for issuance date

    def __str__(self):
        return self.name