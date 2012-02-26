from django.http import HttpResponse
import urllib2, urllib, json
from nursery.settings import pw_salt, request_salt
import datetime
import hashlib
from nursery.logic.models import UserProfile, AuthenticationError
from nursery.logic.models import Authenticate

def test_create_nursery(request):
    host_url = "http://173.255.192.81/api/nursery/"
    user_id = 3 #aleksey's id
    password = 'aleksey'
    password_hash = hashlib.md5(pw_salt + password).hexdigest()
    now = datetime.datetime.now()
    #strTime = now.strftime("%Y-%m-%d %H:%M:%S")
    strTime = '2012-02-91 12:23:42'
    request_hash = hashlib.md5(request_salt + strTime + password_hash).hexdigest()
    request_data = {'user_id':user_id, 'request_hash':request_hash,
                    'params': {'name': 'nursery1', 'country':'USA', 'state':'CAL', 'city':'CAL', 'address':'address1', 'zipcode':'zipcode1', 'phonenumber':'444-444-4444'} }
    data = json.dumps(request_data)
    #return HttpResponse(data)
    req = urllib2.Request(host_url, data, {"Content-type": "application/json"})
    response_stream = urllib2.urlopen(req)
    
    response = response_stream.read()
    #return HttpResponse("test create nursery")
    return HttpResponse(response)

def test(request):
    user_id = 6
    request_hash = 'abc'
    if Authenticate(user_id, request_hash) == True:
        return HttpResponse('True')
    return HttpResponse('False')

