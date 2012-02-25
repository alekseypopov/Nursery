from django.conf.urls.defaults import *
from nursery.testapi.views import test_create_nursery

urlpatterns = patterns('',
    url('^nursery/$', test_create_nursery),
)

