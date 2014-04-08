import datetime
from django.views import generic
from .models import Slide, Section

TALK_SECONDS = 1620.0


class ListView(generic.ListView):

    model = Slide
    context_object_name = 'slides'
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['time_per_slide'] = self.get_queryset().count()/TALK_SECONDS
        return context

    def get_queryset(self):
        queryset = super(ListView, self).get_queryset()
        return queryset.filter(is_enabled=True)


class VersionListView(generic.ListView):

    model = Slide
    context_object_name = 'slides'
    template_name = 'base.html'

    # def __init__(self, *args, **kwargs):
    #     super(VersionListView, self).__init__(*args, **kwargs)
    #     kwargs[]

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['time_per_slide'] = self.get_queryset().count()/TALK_SECONDS
        context['A'] = self.get_queryset().filter(versionA=True).count()
        context['A_time'] = self.get_queryset().filter(versionA=True).count()/TALK_SECONDS
        context['B'] = self.get_queryset().filter(versionB=True).count()
        context['B_time'] = self.get_queryset().filter(versionB=True).count()/TALK_SECONDS
        context['C'] = self.get_queryset().filter(versionC=True).count()
        context['C_time'] = self.get_queryset().filter(versionC=True).count()/TALK_SECONDS
        return context

    def get_queryset(self):
        queryset = super(VersionListView, self).get_queryset()
        if self.kwargs['version'] == 'A':
            queryset = queryset.filter(is_enabled=True).exclude(versionB=False,versionC=False)
        if self.kwargs['version'] == 'B':
            queryset = queryset.filter(is_enabled=True).exclude(versionA=False,versionC=False)
        if self.kwargs['version'] == 'C':
            queryset = queryset.filter(is_enabled=True).exclude(versionA=False,versionB=False)
        return queryset


class SectionDetailView(generic.DetailView):

    model = Section
    template_name = 'base.html'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(SectionDetailView, self).get_context_data(**kwargs)
        slides = Slide.objects.filter(is_enabled=True)
        context['slides'] = slides.filter(section=self.get_object())
        len_sections = Section.objects.count()
        context['time_per_slide'] = TALK_SECONDS/slides.count()
        section_time = TALK_SECONDS/len_sections
        context['time_per_section'] = datetime.timedelta(seconds=section_time).__str__()
        return context