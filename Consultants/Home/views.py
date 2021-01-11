from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        'variables' : 'This is sent from variables',
        'variables1' : 'This my variable 1'
    }
    return render (request, "index.html", context)
    # return HttpResponse("This is a Homepage")


def about(request):
    return render (request, "about.html")
    # return HttpResponse("This is a aboutpage")


def contact(request):
    return render (request, "contact.html" )
    # return HttpResponse("This is a Contactpage")


def services(request):
    return render (request, "services.html" )
    # return HttpResponse("This is a servicespage")