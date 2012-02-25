from django.http import HttpResponse
import urllib2, urllib, json
from nursery.settings import pw_salt, request_salt
import datetime
import md5

def test_create_nursery(request):
    host_url = "http://173.255.192.81/api/nursery"
    user_id = 3 #aleksey's id
    password = 'aleksey'
    password_hash = md5(pw_salt + password)
    now = datetime.datetime.now()
    strTime = now.strftime("%Y-%m-%d %H:%M:%S")
    request_hash = md5(request_salt + strTime + password_hash)
    
    request_data = {'user_id':user_id, 'request_hash':request_hash,
                    'params': {'name': 'nursery1', 'country':'USA', 'state':'CAL', 'address':'address1', 'zipcode':'zipcode1', 'phonenumber':'444-444-4444'} }
    data = json.dumps(request_data)
    req = urllib2.Request(host_url, data, {"Content-type": "application/json"})
    response_stream = urllib2.urlopen(req)
    response = response_stream.read()
    #return HttpResponse("test create nursery")
    return HttpResponse(response)


