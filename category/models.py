from django.db import models
from menu.models import Menu


class Category(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)