from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h1>Hello, world!</h1>")

def user_page(request, user_name):
    return HttpResponse(
        f"<h1>Hello, {user_name}!</h1>"
    )
