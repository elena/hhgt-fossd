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
        'order',
        'content',
        'helper',
        'header',
        'bg_img',
        'percent_complete',
        'style',
        'colour_scheme',
        'is_enabled',
        'section',
        'slide_id',

        'notes',
    ]
    extra = 0
    can_delete = True


def show_slide_count(self):
    return self.slide_set.count()

class SectionAdmin(admin.ModelAdmin):

    fieldsets = [(None, {'fields': (('title', 'order', 'colour_scheme'),)})]
    inlines = [SlideInlines]
    list_display = ['title', 'order', 'talk', show_slide_count]
    list_editable = ['order']# , 'talk']


admin.site.register(Section, SectionAdmin)


class SlideAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = [
        'order',
        'content',
        'helper',
        'header',
        'section',
        'percent_complete',
        'style',
        'colour_scheme',
        'slide_id',
        # 'versionA',
        # 'versionB',
        # 'versionC',
        #'is_enabled',
        'bg_img',
        'talk',
        'notes',

    ]
    list_editable = [
        'percent_complete',
        'content',
        'section',
        'helper',
        'style',
        # 'colour_scheme',
        # 'versionA',
        # 'versionB',
        # 'versionC',
        'slide_id',
        'header',
        'order',
        'bg_img',
        # 'is_enabled',
        'notes',
    ]
    list_display_links = [
        'talk',
    ]


admin.site.register(Slide, SlideAdmin)
