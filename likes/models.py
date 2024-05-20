# likes/models.py

from django.db import models
from django.contrib.auth.models import User  # Import the User model

class Like(models.Model):
    # Define your fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # Other fields...

    


