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


class SectionDetailView(generic.DetailView):

    model = Section
    template_name = 'base.html'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(SectionDetailView, self).get_context_data(**kwargs)
        slides = Slide.objects.all()
        context['slides'] = slides.filter(section=self.get_object())
        len_sections = Section.objects.count()
        context['time_per_slide'] = TALK_SECONDS/slides.count()
        section_time = TALK_SECONDS/len_sections
        context['time_per_section'] = datetime.timedelta(seconds=section_time).__str__()
        return context