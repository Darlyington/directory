from django.db import models
from django.utils import timezone

class NewsUpdate(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='news/', null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class ContactUs(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Store(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='store_images/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name