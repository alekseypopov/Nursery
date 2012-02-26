from piston.handler import BaseHandler
from nursery.logic.models import Nursery, UserProfile
import json
import datetime
from nursery.logic.models import Authenticate
from nursery.logic.models import Greenhouse
from django.http import HttpResponse

class CreateNursery_Handler(BaseHandler):
    '''
    This class is for creating new nursery.
    URI: POST /api/nursery/
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
                
class CreateGreenhouse_Handler(BaseHandler):
    '''
    This class is for creating new greenhouse.
    URI: POST /api/nursery/(nursery_id)/addGreenhouse/
    URI Sample : /api/nursery/3/addGreenhouse/
    '''
    allowed_methods = ('POST',)
    
    def create(self, request, nursery_id):
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
                params = request_data['params']
                name = params['name']
                desc = params['desc']
                latitude = params['latitude']
                longitude = params['longitude']
                
                try:
                    greenhouse = Greenhouse.objects.filter(name=name,
                                                           desc=desc,
                                                           latitude=latitude,
                                                           longitude=longitude,
                                                           nursery__id_exact=nursery_id,
                                                           isDeleted = False
                                                           )
                    if len(greenhouse) != 0:
                        r_value = json.dumps({'result': 'Nursery Already Exist'})
                        return HttpResponse(r_value)
                except:
                    dateCreated = datetime.datetime.now()
                    dateModified = dateCreated
                            
                    nursery = None        
                    try:
                        nursery = Nursery.objects.get(id=nursery_id)
                    except:
                        r_value = json.dumps({'result': 'Nursery ID invalid'})
                        return HttpResponse(r_value)
                    
                    new_gs = Greenhouse(name=name, desc=desc, latitude=latitude, longitude=longitude, 
                                        dateCreated=dateCreated, dateModified=dateModified, nursery=nursery, isDeleted=False)
                    new_gs.save()
                    strTime = dateCreated.strftime("%Y-%m-%d %H:%M:%S")
                    r_value = json.dumps({'result': {'id': new_gs.id, 'dateCreated': strTime}})
                    return HttpResponse(r_value)
            r_value = json.dumps({'result': 'Auth Failed'})
            return HttpResponse(r_value)
