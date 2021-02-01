from django.db import models

# Create your models here.

class Note(models.Model):
	title		= models.CharField(max_length=150) # max_length = required
	description	= models.TextField(blank=True, null= True)