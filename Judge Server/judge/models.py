from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from django.utils import timezone
from froala_editor.fields import FroalaField



class Graph(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  event = models.CharField(max_length=100)
  date = models.DateTimeField(default=timezone.now)
  local_rank = models.IntegerField()
  new_rating = models.IntegerField()
  old_rating =models.IntegerField()
  absolute = models.IntegerField()


	
class Problem(models.Model):
    title = models.CharField(max_length=100)
    statement = FroalaField(options={
    'height': 300,'lineHeights': {
      'Default': '',
      'Single': '1',
      '1.15': '1.15',
      '1.5': '1.5',
      'Double': '2'
    }
  },theme='gray',blank='true')
    constraint =FroalaField(options={
    'height': 100,'placeholderText':'e.g.,<br><ul><li>N &gt; 10<sup>9&nbsp;</sup>&nbsp;</li><li>A<sub>1</sub>+A<sub>2</sub>+........+A<sub>N</sub>&nbsp; &gt; 10<sup>18</sup></li></ul>'
  },theme='gray',blank='true')
    input_format = models.TextField()
    output_format = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()
    explaination = models.TextField()
    time_limit = models.IntegerField(default=1)
    difficulty = models.CharField(max_length=10)
    auth = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    input_file = models.FileField(upload_to='inputs/')
    output_file = models.FileField(upload_to='outputs/')
    difficultylevel = models.IntegerField("default=1")

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
      if self.difficulty == "Easy":
         self.difficultylevel=1
      elif self.difficulty == "Medium":
         self.difficultylevel=2
      elif self.difficulty == "Hard":
         self.difficultylevel=3
      else :
         self.difficultylevel=4
      super().save(*args,**kwargs)


class Problem_Feature(models.Model):
    problem = models.OneToOneField(Problem,on_delete = models.CASCADE, primary_key = True)
    accuracy =  models.FloatField(default=0)
    total_submission = models.IntegerField(default=0)

class Problem_Tags(models.Model):
    problem = models.ForeignKey(Problem,on_delete = models.CASCADE)
    tags = models.CharField(max_length=20)

    def __str__(self):
        return self.tags


class Solution(models.Model):
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
    usr = models.ForeignKey(User,on_delete=models.CASCADE)
    language = models.TextField()
    date_submitted = models.DateTimeField(default=timezone.now)
    solution_file = models.FileField(upload_to='solutions/')

class Result(models.Model):
    solution = models.OneToOneField(Solution,on_delete = models.CASCADE, primary_key = True) 
    verdict = models.TextField()
    time = models.TextField()
    message = models.TextField()


