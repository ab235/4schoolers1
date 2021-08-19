from django.db import models

# Create your models here.
class Pet(models.Model):
	name = models.CharField(max_length=20)
	type = models.CharField(max_length=20)

	def __str__(self):
		return "{}: {}".format(self.name, self.type)

	def __repr__(self):
		return "{}: {}".format(self.name, self.type)