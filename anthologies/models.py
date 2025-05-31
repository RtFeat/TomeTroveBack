from django.db import models

class Anthology(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='anthology_images/', null=True, blank=True)
    description = models.TextField()
    topic = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title