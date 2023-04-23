from django.db import models

from tinymce.models import HTMLField



class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
   
    body = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    image = models.ImageField(upload_to="images/%Y/%m/%d", blank=True, null=True)


    def __str__(self):
        return self.title
    