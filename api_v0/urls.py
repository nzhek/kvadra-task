from django.conf.urls import url

from api_v0 import views

urlpatterns = [
    # for public
    url(r'^content/upload-text/$', views.ContentAPI.as_view({'post': 'uploadText'})),
    # for manager
    url(r'^content/remove-text/$', views.ContentAPI.as_view({'post': 'removeText'})),
    url(r'^content/get-text/$', views.ContentAPI.as_view({'get': 'getText'})),
]
