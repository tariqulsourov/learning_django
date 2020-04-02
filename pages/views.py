from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    print(request.user)
    # print(args, kwargs)
    print(request)
    # return HttpResponse("<h1>Hello World </h1>")
    return render(request, "home.html")

def contact_view(request):
    return render(request, "contact.html")
def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 13, 134,134]
    }

    return render(request, "about.html", my_context)

