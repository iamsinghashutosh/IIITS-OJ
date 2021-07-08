from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from froala_editor.fields import FroalaField





class Post(models.Model): 
    title = models.CharField(max_length=100)
    content = FroalaField(theme='gray')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk' : self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    usr = models.ForeignKey(User,on_delete=models.CASCADE)
    date_commented = models.DateTimeField(default=timezone.now)
    user_reaction = models.ManyToManyField(User,related_name='react')
    text = models.TextField()
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.text
    
    



        










    
    
    





    
