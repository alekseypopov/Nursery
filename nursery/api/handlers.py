from piston.handler import BaseHandler
from nursery.logic.models import Nursery, UserProfile
import json
import datetime
from nursery.logic.models import Authenticate

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
        return "Success"
        #first authenticate user
        if request.POST == 'POST':
            request_data = json.loads(request.raw_post_data)
            user_id = request_data['user_id']
            request_hash = request_data['request_hash']
            
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
                
                newNursery = Nursery(name = name,
                                     country = country,
                                     state = state,
                                     city = city,
                                     address = address,
                                     zipcode = zipcode,
                                     PhoneNumber = PhoneNumber,
                                     dateCreated = dateCreated,
                                     dateModified = dateModified,
                                     isActive = isActive,
                                     adminUser = adminUser
                                     )
                strTime = dateCreated.strftime("%Y-%m-%d %H:%M:%S")
                return json.dumps({'result': {'id': newNursery.id, 'dateCreated': strTime}})
            
            return json.dumps({'result': 'Auth Failed'})
                