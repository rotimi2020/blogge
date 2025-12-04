# Create your models here.
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import math

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    is_clicked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name




class Blog_Post(models.Model):
    CATEGORY_CHOICES = [
        ('travel', 'Travel'),
        ('business', 'Business'),
        ('news', 'News'),    
        ('sport', 'Sport'),
        ('health', 'Health'),
        ('food', 'Food'),
        ('mary astor', 'Mary Astor'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)  # new slug field
    content = models.TextField()
    image = models.ImageField(upload_to='blog_headers/', blank=True, null=True)
    author = models.CharField(max_length=100, default="Admin")
    created_at = models.DateTimeField(default=timezone.now)
    reading_time = models.PositiveIntegerField(default=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default ='travel')
    is_top_post = models.BooleanField(default=False)       
    is_trending = models.BooleanField(default=False)  

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        words = self.content.split()
        self.reading_time = math.ceil(len(words)/200)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


        
