from django.views import generic
from .models import Slide, Section

class ListView(generic.ListView):

    model = Slide
    context_object_name = 'slides'
    template_name = 'base.html'


class SectionDetailView(generic.DetailView):

    model = Section
    template_name = 'base.html'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(SectionDetailView, self).get_context_data(**kwargs)
        context['slides'] = Slide.objects.filter(section=self.get_object())
        return context