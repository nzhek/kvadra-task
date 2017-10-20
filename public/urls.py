from django.conf.urls import url

from public.views import *

urlpatterns = [
    url(r'^$', index_view, name='index')
]
