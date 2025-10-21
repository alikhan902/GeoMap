from django.contrib import admin
from geoapp.models import Place, PlaceImage

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'latitude', 'longitude')  
    search_fields = ('title',) 
    
@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('place',)  
    search_fields = ('place',) 