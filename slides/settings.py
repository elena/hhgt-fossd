from django.conf import settings

CURRENT_TALK = getattr(settings, 'CURRENT_TALK', 1)
