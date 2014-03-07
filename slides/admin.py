from django.contrib import admin
from .models import Talk, Section, Slide

admin.site.register(Talk)
admin.site.register(Section)

class SlideAdmin(admin.ModelAdmin):

    extra = 1
    list_display = [
        'talk',
        'section',
        'style',
        'colour_scheme',
        'version',
        'slide_id',
        'header',
        'content',
        'order',
        'is_enabled',
    ]
    list_editable = [
        'section',
        'style',
        'colour_scheme',
        'version',
        'slide_id',
        'header',
    ]


admin.site.register(Slide, SlideAdmin)
