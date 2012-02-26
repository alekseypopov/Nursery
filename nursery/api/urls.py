from django.conf.urls.defaults import *
from piston.resource import Resource
from handlers import CreateNursery_Handler

create_newNursery = Resource(handler = CreateNursery_Handler)
create_newGreenhouse = Resource(handler = CreateGreenhouse_Handler)

urlpatterns = patterns('',
    url('^nursery/$', create_NewNursery),
    url('^nursery/(?P<nursery_id>\d+)/addGreenhouse/$', create_newGreenhouse),
)