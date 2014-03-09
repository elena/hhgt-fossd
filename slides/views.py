from django.views import generic
from .models import Slide

class ListView(generic.ListView):

    model = Slide
    context_object_name = 'slides'
    template_name = 'base.html'