from django.conf import settings
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    location = models.CharField(max_length=255, blank=False, null=False)  
      
    # Reference to custom User model using AUTH_USER_MODEL
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name