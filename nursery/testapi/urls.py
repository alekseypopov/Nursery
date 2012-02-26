from django.conf.urls.defaults import *
from nursery.testapi.views import test_create_nursery, test_create_greenhouse, test

urlpatterns = patterns('',
    url('^addNursery/$', test_create_nursery),
    url('^addGreenhouse/$', test_create_greenhouse),
    url('^test/$', test),
)

