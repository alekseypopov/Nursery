from django.http import HttpResponse

def home(request):
    return HttpResponse("Nursery Management System")

