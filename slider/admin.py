from django.contrib import admin
from django.utils.html import format_html

from slider.models import Slider


from django.utils.html import mark_safe

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('slider_title', 'slider_css', 'slider_image_preview')

    def slider_image_preview(self, obj):
        if obj.slider_image:
            return mark_safe(f'<img src="{obj.slider_image.url}" width="100" />')
        return "(No image)"
    slider_image_preview.short_description = "Preview"
