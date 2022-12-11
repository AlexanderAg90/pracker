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

def show_category(request, category_slug):
    template = loader.get_template('catalog/list.html')
    category = Category.objects.get(slug=category_slug)
    categories = category.get_descendants(include_self=True)
    print(categories)
    context = {
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))