from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    institution = models.CharField(max_length=100,default="IIITS")
    bio = models.TextField(default="...")
    rating=models.IntegerField(default=0)
    hrating=models.IntegerField(default=0)
    star=models.IntegerField(default=1)
    ac_solution=models.IntegerField(default=0)
    wa_solution=models.IntegerField(default=0)
    tle_solution=models.IntegerField(default=0)
    ce_solution=models.IntegerField(default=0)
    re_solution=models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        
        img  = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)