from django.http import HttpResponse
from django.template import loader
from .models import Category

def index(request):
    template = loader.get_template('catalog/list.html')
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))