from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url

from views import auth_tagpro, deauth_tagpro

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.html"), name="home"),
    url(r'^tp_auth/$', auth_tagpro, name="auth_tagpro"),
    url(r'^tp_logout/$', deauth_tagpro, name="deauth_tagpro"),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
