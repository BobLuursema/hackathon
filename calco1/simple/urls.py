from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^regelingen/$', views.regelingen),
    url(r'^suggesties/(?P<naam>.*)/$', views.suggesties),
]