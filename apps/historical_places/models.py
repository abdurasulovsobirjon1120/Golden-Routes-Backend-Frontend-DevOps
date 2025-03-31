from django.db import models


class Country(models.Model):
    country = models.CharField(max_length=100, unique=True, default="Uzbekistan")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country


class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="regions")
    region = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.region}, {self.country}"


class HistoricalPlace(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="historical_places")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="historical_places")
    location = models.CharField(max_length=255) 
    entry_price = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="historical_places/photos/", null=True, blank=True)
    stars = models.FloatField(default=0.0)
    total_reviews = models.IntegerField(default=0) 
    comments = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.region}"

    def update_stars(self, new_rating):
        """O'rtacha bahoni yangilash"""
        total_stars = self.stars * self.total_reviews + new_rating
        self.total_reviews += 1
        self.stars = total_stars / self.total_reviews
        self.save()


class HistoricalFavourite(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="historical_favourites")
    place = models.ForeignKey(HistoricalPlace, on_delete=models.CASCADE, related_name="historical_favourites")

    class Meta:
        unique_together = ('user', 'place') 

    def __str__(self):
        return f"{self.user.username} - {self.place.name}"