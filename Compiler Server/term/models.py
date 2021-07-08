from django.db import models

# Create your models here.
class program(models.Model):
	sol_id=models.TextField()
	# sol_name=models.CharField(max_length=100,blank=False)
	language=models.CharField(max_length=100,blank=False)
	solution=models.FileField(upload_to='./soln')
	def __str__(self):
		return self.sol_name

class author(models.Model):
	sol_id=models.TextField()
	sol_in=models.FileField(upload_to='./media/input')
	sol_out=models.FileField(upload_to='./media/output')
	sol_time=models.IntegerField(blank=False,default=True)
	def __str__(self):
		return self.sol_id

	


	
