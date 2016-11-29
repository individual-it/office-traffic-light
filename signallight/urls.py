from django.conf.urls import url

from . import views

app_name = 'signallight'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<choice_id>[0-9]+)/$', views.select, name='select'),
]
