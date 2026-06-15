from django.http import HttpResponse

def home(request):

    if request.user.is_authenticated:

        return HttpResponse(
            f"Welcome {request.user.username}"
        )

    return HttpResponse(
        "Multi-Agent Research Assistant"
    )