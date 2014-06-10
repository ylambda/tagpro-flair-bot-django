from django.conf.urls import patterns, include, url

from views import auth_tagpro, deauth_tagpro, set_flair, HomeView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^tp_auth/$', auth_tagpro, name="auth_tagpro"),
    url(r'^tp_logout/$', deauth_tagpro, name="deauth_tagpro"),
    url(r'^set_flair/(?P<flair>[-\w]+)/$', set_flair, name="set_flair"),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
