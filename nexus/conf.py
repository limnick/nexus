from django.conf import settings

MEDIA_PREFIX = getattr(settings, 'NEXUS_MEDIA_PREFIX', '/nexus/static/')

if getattr(settings, 'NEXUS_USE_DJANGO_MEDIA_URL', False):
    MEDIA_PREFIX = getattr(settings, 'MEDIA_URL', MEDIA_PREFIX)

USE_STATICFILES = getattr(settings, 'NEXUS_USE_STATICFILES', False)
