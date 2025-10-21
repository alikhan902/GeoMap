from rest_framework import serializers
from .models import Place, PlaceImage

class PlaceSerializer(serializers.ModelSerializer):
    imgs = serializers.SerializerMethodField()
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ('title', 'imgs', 'description_short', 'description_long', 'coordinates')

    def get_imgs(self, obj):
        urls = []
        if obj.main_image:
            urls.append(self.context['request'].build_absolute_uri(obj.main_image.url))
        for img in obj.images.all():
            urls.append(self.context['request'].build_absolute_uri(img.image.url))
        return urls

    def get_coordinates(self, obj):
        return {
            "lat": obj.latitude,
            "lng": obj.longitude
        }
