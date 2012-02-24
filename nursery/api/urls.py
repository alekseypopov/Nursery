from django.conf.urls.defaults import *
from piston.resource import Resource
from handlers import CreateNursery_Handler

create_NewNursery = Resource(handler = CreateNursery_Handler)

urlpatterns = patterns('',
    url('^nursery/$', create_NewNursery),
)