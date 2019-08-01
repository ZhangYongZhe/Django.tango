from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("这是一个测试视图！！！")

def about(repuest):
    return HttpResponse("Rango says here is the about page.!!!")



