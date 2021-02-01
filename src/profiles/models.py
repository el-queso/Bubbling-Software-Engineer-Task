from django.db import models

# Create your models here.

class Profile(models.Model):
	title		= models.CharField(max_length=120) #max_length = required
	description = models.TextField(blank=True, null=True)