from django.conf.urls.defaults import patterns, include, url
from mgmt import views

urlpatterns = patterns('mgmt.views',

    url(r'^begins/$', 'db_init', name="init"),
)
