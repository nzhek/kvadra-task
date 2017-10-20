from django.conf.urls import url
from django.contrib.auth import views
from manager.forms import LoginForm

from manager.views import *


urlpatterns = [
    url(r'^$', index_view, name='index-admin'),
    url(r'^detail/(?P<element_code>.*)/$', detail_view, name='detail'),
    url(r'^login/$', views.login, {'template_name': 'manager/login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', views.logout, {'next_page': '/manager/login/'}),
]
