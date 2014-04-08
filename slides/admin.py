from django.contrib import admin
from django.utils.text import Truncator
from django.utils.html import strip_tags, linebreaks
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
        'pk',
        'order_abs',
        'order',
        'show_content',
        #'content',
        'helper',
        'header',
        'section',
        'colour_scheme',
        'percent_complete',
        #'style',
        #'bg_img',
        #'slide_id',
        'versionA',
        'versionB',
        'versionC',
        'is_enabled',
        #'talk',
        #'notes',

    ]
    list_editable = [
        #'bg_img',
        #'content',
        #'header',
        #'helper',
        #'notes',
        #'slide_id',
        #'style',
        'colour_scheme',
        'is_enabled',
        'order',
        'percent_complete',
        'section',
        'versionA',
        'versionB',
        'versionC',
    ]
    list_filter = ['is_enabled', 'section', 'colour_scheme']
    list_display_links = [
        'pk',
    ]

    def show_content(self, obj):
        return u"<div style='white-space:nowrap'>{0}</div>".format(strip_tags(Truncator(obj.content).words(20, html=True, truncate=' ...')))
        #return u"<div style='white-space:nowrap'>{0}</div>".format(linebreaks(strip_tags(Truncator(obj.content).words(20, html=True, truncate=' ...'))))
    show_content.allow_tags = True

    def show_notes(self, obj):
        return u"<div style='white-space:nowrap'>{0}</div>".format(linebreaks(strip_tags(Truncator(obj.content).words(20, html=True, truncate=' ...'))))
    show_notes.allow_tags = True


admin.site.register(Slide, SlideAdmin)
