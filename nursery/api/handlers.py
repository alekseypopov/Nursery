from piston.handler import BaseHandler
from nursery.logic.models import Nursery, UserProfile
import json
import datetime
from nursery.logic.models import Authenticate
from django.http import HttpResponse

class CreateNursery_Handler(BaseHandler):
    '''
    This class is for creating new nursery.
    URI: POST /api/nursery
    '''
    
    model = Nursery
    allowed_methods = ('POST',)
    
    def create(self, request):
        '''
        Creats a new nursery
        '''
        #first authenticate user
        if request.method == 'POST':
            request_data = json.loads(request.raw_post_data)
            user_id = request_data['user_id']
            request_hash = request_data['request_hash']

            #return HttpResponse("True")
            #first of all, authenticate user
            if Authenticate(user_id, request_hash) == True:
                #this means proper user
                params = request_data['params']
                name = params['name']
                country = params['country']
                state = params['state']
                city = params['city']
                address = params['address']
                zipcode = params['zipcode']
                PhoneNumber = params['phonenumber']
                dateCreated = datetime.datetime.now()
                dateModified = dateCreated
                isActive = False
                adminUser = UserProfile.objects.get(user__id__exact = user_id)
                
                newNursery = None
                exist = None
                
                exist = Nursery.objects.filter(name = name,
                                 country = country,
                                 state = state,
                                 city = city,
                                 address = address,
                                 zipcode = zipcode,
                                 phoneNumber = PhoneNumber)
                
                if len(exist) != 0:
                    r_value = json.dumps({'result': 'Nursery Already Exist'})
                    return HttpResponse(r_value)  
               
                newNursery = Nursery(name = name,
                                 country = country,
                                 state = state,
                                 city = city,
                                 address = address,
                                 zipcode = zipcode,
                                 phoneNumber = PhoneNumber,
                                 dateCreated = dateCreated,
                                 dateModified = dateModified,
                                 isActive = isActive,
                                 adminUser = adminUser
                                 )
                newNursery.save()
                strTime = dateCreated.strftime("%Y-%m-%d %H:%M:%S")
                r_value = json.dumps({'result': {'id': newNursery.id, 'dateCreated': strTime}})
                return HttpResponse(r_value)
            
            r_value = json.dumps({'result': 'Auth Failed'})
            return HttpResponse(r_value)
                