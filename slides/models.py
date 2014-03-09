# -*- coding: utf-8 -*-
from django.db import models
from .settings import CURRENT_TALK

CHOICES_COLOUR = (
    ('', ''),
    ('1', 'blue'),
    ('2', 'green'),
    ('3', 'red'),
)


class Talk(models.Model):
    talk = models.CharField(max_length=128, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    event = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.talk


class Section(models.Model):
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
        ('', ''),
        ('cover', 'cover'),
        ('shout', 'shout'),
    )

    CHOICES_VERSION = (
        ('sigma', 'Σ'),
        ('cappa', 'Κ'),
        ('delta', 'Δ'),
    )

    talk = models.ForeignKey(Talk, blank=True, default=CURRENT_TALK)
    section = models.ForeignKey(Section)

    # A, B or C
    #version = models.ManyToManyField(Version, null=True, blank=True)
    versionA = models.BooleanField(default=False, verbose_name="A")
    versionB = models.BooleanField(default=False, verbose_name="B")
    versionC = models.BooleanField(default=False, verbose_name="C")

    # considering making following fields all FK
    slide_id = models.CharField(max_length=128, blank=True)
    style = models.CharField(max_length=128, choices=CHOICES_CLASS, blank=True)
    colour_scheme = models.CharField(choices=CHOICES_COLOUR, max_length=32, blank=True)

    order = models.IntegerField(blank=True, null=True)

    # duration approximately
    # can't decided if time, seconds or float.
    time = models.IntegerField(blank=True, null=True)

    header = models.CharField(max_length=256, blank=True)
    content = models.TextField(blank=True)

    is_enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return '{0} {1:02} {2}'.format(self.section, self.order, self.slide_id)
