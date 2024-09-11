from django.shortcuts import render, HttpResponse, redirect

# Create your views here.



def index (request):
    return render(request, "index.html") 


def createUser (request):
    return render(request, "createUser.html") 

def page (request):
     return render(request, "page.html") 


def contact (request):
     return render(request, "contact.html") 