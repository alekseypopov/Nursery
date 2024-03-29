from django.db import models
from django.contrib.auth.models import User
from nursery.settings import pw_salt, request_salt
import datetime
import hashlib

class UserProfile(models.Model):
    '''
        User model has a "username". But we don't need username, but email address
        because username is required field, we'll fill-in username by email.
        email is unique, and it satisfies "unique" and "required" condition for username
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    street = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    zipcode = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=24)
    website = models.URLField(blank=True)
    business_type = models.CharField(max_length=10)
    dateCreated = models.DateTimeField()
    dateModified = models.DateTimeField() 
    
class Nursery(models.Model):
    name = models.CharField(max_length=128, unique=True)
    country = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    zipcode = models.CharField(max_length=32)
    phoneNumber = models.CharField(max_length=24)
    dateCreated = models.DateTimeField()
    dateModified = models.DateTimeField()
    isActive = models.BooleanField()
    adminUser = models.ForeignKey(UserProfile, blank=True, null=True, default=null)
    #payment = models.ForeignKey(Payment)
    
class Greenhouse(models.Model):
    name = models.CharField(max_length=256)
    desc = models.CharField(max_length=256)
    latitude = models.CharField(max_length=64)
    longitude = models.CharField(max_length=64)
    dateCreated = models.DateTimeField()
    dateModified = models.DateTimeField()
    nursery = models.ForeignKey(Nursery)
    isDeleted = models.BooleanField()

class ScientificName(models.Model):
    name = models.CharField(max_length = 256)
    description = models.CharField(max_length = 1024)
        
class Plant(models.Model):
    plantName = models.CharField(max_length=256)
    plantSize = models.FloatField() # what's the unit of size?
    plantHeight = models.FloatField()
    plantType = models.CharField(max_length=64)
    plantImage = models.FilePathField()
    trunkDiameter = models.FloatField()
    variety = models.IntegerField()
    isAvailable = models.BooleanField()
    isBlooming = models.BooleanField()
    notes = models.CharField(max_length=1024)
    price = models.FloatField()
    scientificName = models.ForeignKey(ScientificName) #must be decided if adopt ScientificName table or not.
    stock = models.CharField(max_length=64)
    dateCreated = models.DateTimeField()
    dateModified = models.DateTimeField()
    datePictureLastUpdated = models.DateTimeField()
    greenhouse = models.ForeignKey(Greenhouse)


class AuthenticationError(Exception):
    pass

def Authenticate(user_id, request_hash):
    '''
    Authentication Algorithm:
        server_password_hash = md5(pw_salt + userpassword)
        server_request_hash = md5(request_salt + datetime.today() + server_password_hash)
        if server_request_hash == request_hash:
            Success
        else:
            Fraud.
    '''
    user = None
    try:
        user = UserProfile.objects.get(id__exact = user_id)
    except:
        #raise AuthenticationError("unregistered user")
        return False
    password_hash = hashlib.md5(pw_salt + user.password).hexdigest()
    now = datetime.datetime.now()
    #strTime = now.strftime("%Y-%m-%d %H:%M:%S")
    strTime = '2012-02-91 12:23:42'
    server_request_hash = hashlib.md5(request_salt + strTime + password_hash).hexdigest()
    if server_request_hash == request_hash:
        return True
    return False

def Authenticate_ByEmail(email, request_hash):
    '''
    Authentication Algorithm:
        same as above Authenticate function
    '''
    user = None
    try:
        user = UserProfile.objects.get(email__exact = email)
    except:
        #raise AuthenticationError("unregistered user")
        return False
    password_hash = hashlib.md5(pw_salt + user.password).hexdigest()
    now = datetime.datetime.now()
    #strTime = now.strftime("%Y-%m-%d %H:%M:%S")
    strTime = '2012-02-91 12:23:42'
    server_request_hash = hashlib.md5(request_salt + strTime + password_hash).hexdigest()
    if server_request_hash == request_hash:
        return True
    return False
