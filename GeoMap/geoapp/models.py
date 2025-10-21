from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.TextField(blank=True)
    description_long = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    main_image = models.ImageField(blank=True, upload_to='places/')

class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='places/')
    