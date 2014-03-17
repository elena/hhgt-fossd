from django.contrib import admin
from .models import Talk, Section, Slide


class SectionInlines(admin.TabularInline):

    model = Section
    extra = 1


class TalkAdmin(admin.ModelAdmin):

    #fieldsets = [(None, {'fields': (('title', 'order', 'colour_scheme'),)})]
    inlines = [SectionInlines]

admin.site.register(Talk, TalkAdmin)


class SlideInlines(admin.TabularInline):

    model = Slide
    fields = [
        'percent_complete',
        'content',
        'notes',
        'order',
        'header',
        'style',
    ]
    extra = 1
    can_delete = True


class SectionAdmin(admin.ModelAdmin):

    fieldsets = [(None, {'fields': (('title', 'order', 'colour_scheme'),)})]
    inlines = [SlideInlines]
    list_display = ['title', 'order', 'talk']
    list_editable = ['order']# , 'talk']


admin.site.register(Section, SectionAdmin)


class SlideAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = [
        'percent_complete',
        'content',
        'notes',
        'header',
        'section',
        'order',
        'style',
        'colour_scheme',
        'slide_id',
        # 'versionA',
        # 'versionB',
        # 'versionC',
        #'is_enabled',
        'talk',
    ]
    list_editable = [
        'percent_complete',
        'content',
        'section',
        'notes',
        'style',
        # 'colour_scheme',
        # 'versionA',
        # 'versionB',
        # 'versionC',
        'slide_id',
        'header',
        'order',
        # 'is_enabled',
    ]
    list_display_links = [
        'talk',
    ]


admin.site.register(Slide, SlideAdmin)
