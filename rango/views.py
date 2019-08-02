from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'boldmessage':"Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(repuest):
    return HttpResponse("Rango says here is the about page.!!!")

def head(repuest):
    context_dict = {'boldmessage' : "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(repuest, 'rango/test2.html',  context=context_dict)


