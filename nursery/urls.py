from django.conf.urls.defaults import patterns, include, url
from nursery.logic.views import home

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nursery.views.home', name='home'),
    # url(r'^nursery/', include('nursery.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^testapi/', include('nursery.testapi.urls')),
    url(r'^api/', include('nursery.api.urls')),
)
