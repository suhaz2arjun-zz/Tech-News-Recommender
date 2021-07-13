from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.enums import Choices
from multiselectfield import MultiSelectField

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    my_choice=(('python','python'),
        ('JS','JS'),
        ('ml','ml'),
        ('java','java'),
        ('hacking','hacking')
    
    )
    interest=MultiSelectField(choices=my_choice)
    objects = models.Manager()

    def _str_(self):
        return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
        super(Profile,self).save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
    # def ready(self):
    #     from .signals import create_profile,save_profile
    #     return Profile.objects.all()