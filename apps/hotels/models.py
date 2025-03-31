from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100, null=False)
    working_time = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, null=False)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)
    stars = models.FloatField(blank=True, null=True)
    favourite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'