from django.db import models

# Create your models here.
class author(models.Model):
	solution=models.FileField(upload_to='./soln_key')
	


	def __str__(self):
		return self.ques_name