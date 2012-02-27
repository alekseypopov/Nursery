from piston.handler import BaseHandler
from nursery.logic.models import Nursery, UserProfile
import json
import datetime
from nursery.logic.models import Authenticate
from nursery.logic.models import Greenhouse
from django.http import HttpResponse
from nursery.logic.models import Authenticate_ByEmail

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
                nursery = None        
                try:
                    nursery = Nursery.objects.get(id=nursery_id)
                except:
                    r_value = json.dumps({'result': 'Nursery ID invalid'})
                    return HttpResponse(r_value)
                
                params = request_data['params']
                name = params['name']
                desc = params['desc']
                latitude = params['latitude']
                longitude = params['longitude']
                
                greenhouse = Greenhouse.objects.filter(name=name,
                                                       desc=desc,
                                                       latitude=latitude,
                                                       longitude=longitude,
                                                       nursery__id=nursery_id,
                                                       isDeleted = False
                                                       )
                if len(greenhouse) != 0:
                    r_value = json.dumps({'result': 'Nursery Already Exist'})
                    return HttpResponse(r_value)
            
                dateCreated = datetime.datetime.now()
                dateModified = dateCreated
                
                new_gs = Greenhouse(name=name, desc=desc, latitude=latitude, longitude=longitude, 
                                    dateCreated=dateCreated, dateModified=dateModified, nursery=nursery, isDeleted=False)
                new_gs.save()
                strTime = dateCreated.strftime("%Y-%m-%d %H:%M:%S")
                r_value = json.dumps({'result': {'id': new_gs.id, 'dateCreated': strTime}})
                return HttpResponse(r_value)
            r_value = json.dumps({'result': 'Auth Failed'})
            return HttpResponse(r_value)

class Login_Handler(BaseHandler):
    '''
    This class is for login process.
    input parameters are email and request_hash generated from password.
    return values are user_id and isAdmin flag.
        if isAdmin is true, then user's nursery id must be returned also.
    '''
    allowed_methods = ('POST')
    def create(self, request):
        request_data = json.loads(request.raw_post_data)
        email = request_data['email']
        request_hash = request_data['request_hash']
        if Authenticate_ByEmail(email, request_hash) == True:
            user = UserProfile.objects.get(user__email__exact = email)
            r_value = {}
            r_value[user_id] = user.user.id
            r_value[first_name] = user.user.first_name
            r_value[last_name] = user.user.last_name
            r_value[phone_number] = user.phoneNumber
            
            nursery = Nursery.objects.filter(adminUser__user__id__exact = r_value[user_id])
            if len(nursery) != 0:
                r_value[isAdmin] = 'True'
                r_value[nursery_id] = nursery.id
            else:
                r_value[isAdmin] = 'False'
            
            result = json.dumps(r_value)
            return HttpResponse(result)
        
        r_value = json.dumps({'result': 'Auth Failed'})
        return HttpResponse(r_value)
            
class AddAdminUser_Handler(BaseHandler):
    '''
            This class is for registering admin user of nursery.
            each nursery can have only one nursery.
            
            input parameter:
                nursery_name:
                first_name, last_name
                email_address
                password
                street, state, city, zipcode, country
                phone_number
                website(optional)
                business_type
    '''
    allowed_methods = ('POST')
    def create(self, request):
        request_data = json.loads(request.raw_post_data)
        nursery = Nursery.objects.filter(name = request_data['nursery_name'])
        if len(nursery) != 1:
            result = json.dumps({'Failed':'No Nursery'})
            return HttpResponse(result)
        if nursery.admin != null:
            result = json.dumps({'Failed':'Admin user already exist'})
            return HttpResponse(result)
        email = request_data['email_address']
        first_name = request_data['first_name']
        last_name = request_data['last_name']
        password = request_data['password']
        
        user = UserProfile()