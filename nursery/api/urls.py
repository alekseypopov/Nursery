from django.conf.urls.defaults import *
from piston.resource import Resource
from handlers import CreateNursery_Handler, CreateGreenhouse_Handler
from handlers import Login_Handler

create_newNursery = Resource(handler = CreateNursery_Handler)
create_newGreenhouse = Resource(handler = CreateGreenhouse_Handler)
user_login = Resource(handler = Login_Handler)
user_addAdminUser = Resource(handler = AddAdminUser_Handler)

urlpatterns = patterns('',
    url('^nursery/$', create_newNursery),
    url('^nursery/(?P<nursery_id>\d+)/addGreenhouse/$', create_newGreenhouse),
    url('^/user/login/$', user_login),
    url('^/user/addAdminUser/$', user_addAdminUser),
)