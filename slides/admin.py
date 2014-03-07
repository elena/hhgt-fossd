from django.contrib import admin
from .models import Slide


class SlideAdmin(models.ModelAdmin):

    list_display = [
        'style',
        'colour_scheme',
        'version',
        'version',

    ]


admin.site.register(Slide, SlideAdmin)
