from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, world.</h1> <p>You're at the pools index</p>")
