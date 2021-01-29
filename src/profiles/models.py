from django.db import models

# Create your models here.

class Profile(models.Model):
	name 		= models.CharField(max_length=50)  # max_length = required
	description = models.TextField()
	email		= models.EmailField(default='email@email.com')
	summary		= models.TextField(blank=True, null=False)
	featured 	= models.BooleanField()  #null=True, default=True
