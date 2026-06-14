from django.http import HttpResponse

def home(request):
    return HttpResponse("Multi-Agent Research Assistant")