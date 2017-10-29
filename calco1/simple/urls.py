from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^regelingen/$', views.regelingen),
    url(r'^suggesties/(?P<id>[0-9]+)/$', views.suggesties),
    url(r'^persoon/(?P<id>[0-9]+)/$', views.persoon),
]