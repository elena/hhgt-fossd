from django import forms
from django.contrib import admin
from .models import Talk, Section, Slide


admin.site.register(Talk)
admin.site.register(Section)


class SlideAdminForm(forms.ModelForm):

    class Meta:
        model = Slide

    def __init__(self):
        widgets = {
           'content' : forms.Textarea(attrs={'class':'cke_editable cke_editable_inline cke_contents_ltr'}),
        }


class SlideAdmin(admin.ModelAdmin):
    form = SlideAdminForm
    save_on_top = True
    list_display = [
        'content',
        'header',
        'slide_id',
        'talk',
        'section',
        'style',
        'colour_scheme',
        'versionA',
        'versionB',
        'versionC',
        'order',
        'is_enabled',
    ]
    list_editable = [
        'content',
        'section',
        'style',
        'colour_scheme',
        'versionA',
        'versionB',
        'versionC',
        'slide_id',
        'header',
        'is_enabled',
    ]
    list_display_links = [
        'talk',
    ]


admin.site.register(Slide, SlideAdmin)
