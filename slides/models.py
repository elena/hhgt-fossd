# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Max
from .settings import CURRENT_TALK

CHOICES_COLOUR = (
    ('blue', 'technical (b)'),
    ('white', 'advice (w)'),
    ('green', 'info (g)'),
    ('red', 'pointed (r)'),
    ('yellow', 'explain (y)'),
)

class Talk(models.Model):
    talk = models.CharField(max_length=128, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    event = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.talk

    class Meta:
        ordering = ['-date']


class Section(models.Model):
    talk = models.ForeignKey('slides.Talk', null=True, blank=True)
    title = models.CharField(max_length=128, blank=True)
    order = models.IntegerField(blank=True, null=True)
    colour_scheme = models.CharField(choices=CHOICES_COLOUR, max_length=32, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Version(models.Model):
    version = models.CharField(max_length=32)

    def __str__(self):
        return self.version


class Slide(models.Model):
    """
    """

    CHOICES_CLASS = (
        ('cover', 'cover'),
        ('shout', 'shout'),
    )

    CHOICES_VERSION = (
        ('sigma', 'Σ'),
        ('delta', 'Δ'),
        ('cappa', 'Κ'),
    )

    CHOICES_COMPLETE = (
        ('0', 'zero'),
        ('25', '25%'),
        ('50', '50%'),
        ('75', '85%'),
        ('100', 'done!'),
    )

    talk = models.ForeignKey('slides.Talk', blank=True, default=CURRENT_TALK)
    section = models.ForeignKey('slides.Section')

    # A, B or C
    #version = models.ManyToManyField(Version, null=True, blank=True)
    versionA = models.BooleanField(default=False, verbose_name="A")
    versionB = models.BooleanField(default=False, verbose_name="B")
    versionC = models.BooleanField(default=False, verbose_name="C")

    # considering making following fields all FK
    slide_id = models.CharField(max_length=128, blank=True)
    style = models.CharField(max_length=128, choices=CHOICES_CLASS, blank=True)
    colour_scheme = models.CharField(choices=CHOICES_COLOUR, max_length=32,
                                     blank=True)

    order = models.IntegerField(blank=True, null=True)

    # duration approximately
    # can't decided if time, seconds or float.
    time = models.IntegerField(blank=True, null=True)

    header = models.CharField(max_length=256, blank=True)
    content = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    helper = models.CharField(max_length=2048, blank=True)
    bg_img = models.CharField(max_length=256, blank=True)

    percent_complete = models.CharField(max_length=32, choices=CHOICES_COMPLETE,
                                        default=0, blank=True,
                                        verbose_name='done')
    is_enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ['section__order', 'order']

    def __str__(self):
        return '%s-%2d (%s)' % (self.section, self.order, self.slide_id)

    def save(self, *args, **kwargs):
        super(Slide, self).save(*args, **kwargs)
        if not self.order:
            # if hasattr(self, 'section'):
            #     slides = Slide.objects.filter(talk=self.talk, section=self.section)
            # else:
            slides = Slide.objects.filter(talk=self.talk)

            highest = slides.aggregate(Max('order'))['order__max']
            self.order = highest + 1
            self.save()