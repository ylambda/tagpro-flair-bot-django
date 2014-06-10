from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.html"), name="home"),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
