from django.http import HttpResponse

def index(request):
    return HttpResponse('<a href="catalog/">Catalog</a>')