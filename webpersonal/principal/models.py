from django.db import models

# Create your models here.

class ClassName(models.Model):
		nombre = models.CharField(max_length = 255)
		descripcion = models.CharField(max_length = 255)