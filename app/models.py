from django.db import models

# Create your models here.
class Estados(models.Model):
    Estado = models.CharField(max_length=45)
