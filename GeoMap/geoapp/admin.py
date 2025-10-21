from django.contrib import admin
from django.utils.html import format_html
from .models import Place, PlaceImage

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1
    readonly_fields = ('image_preview',)  # показываем превью
    fields = ('image', 'image_preview')   # порядок полей в Inline

    # мини-превью изображения
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.image.url)
        return "-"
    image_preview.short_description = "Превью"

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]
    list_display = ('title', 'latitude', 'longitude')
