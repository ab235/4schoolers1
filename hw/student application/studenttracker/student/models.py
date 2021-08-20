from django.db import models

# Create your models here.
class Student(models.Model):
	fn = models.CharField(max_length = 30)
	ln = models.CharField(max_length = 30)
	uname = models.CharField(max_length = 30)
	password = models.CharField(max_length = 30)
	coo = models.CharField(max_length = 100)

	def __str__(self):
		return "Username {}: Student {} {} from {}".format(self.uname, self.fn, self.ln, self.coo)
	def __repr__(self):
		return "Username {}: Student {} {} from {}".format(self.uname, self.fn, self.ln, self.coo)