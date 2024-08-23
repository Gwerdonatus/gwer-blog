from django.db import models
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    date = models.DateField(auto_now_add=True)
    banner = models.ImageField(upload_to='banner/', default='fallback.png', blank=True)

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

def __str__(self):
    return self.title


    

  