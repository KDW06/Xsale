from django.shortcuts import render, HttpResponse

# Create your views here.

def index (request):
    return HttpResponse("""

<h1>Index</h1>

""")


def createUser (request):
    return HttpResponse("""
        <h1>View to create an user</h1>
                        """)

def page (request):
     return HttpResponse("""
        <h1>View Page</h1>
                        """)