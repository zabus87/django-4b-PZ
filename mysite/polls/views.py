from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're ate the polls index")
