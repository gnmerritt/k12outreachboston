from django.http import HttpResponse


def index(req):
    return HttpResponse("Hello program index page")
