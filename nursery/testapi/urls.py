from django.conf.urls.defaults import *
from nursery.testapi.views import test_create_nursery, test

urlpatterns = patterns('',
    url('^nursery/$', test_create_nursery),
    url('^test/$', test),
)

