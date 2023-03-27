from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    post_image = models.ImageField(upload_to='post-images', blank=True, null=True)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    created_on = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
   
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING , related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title