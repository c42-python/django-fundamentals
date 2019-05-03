from django.http.response import HttpResponse

# what django calls 'view' is equivalent of controllers in other frameworks
# this is a function based view; we could also write views using classes
def welcome(request):
    return HttpResponse('Hello, world from Django!')