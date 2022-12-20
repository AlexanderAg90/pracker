from django.http import HttpResponse, Http404
from django.template import loader
from .models import Category, Product

def index(request):
    template = loader.get_template('catalog/list.html')
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))

def show_category(request, category_slug):
    category = None
    try:
        category = Category.objects.get(slug=category_slug)
    except:
        raise Http404("Ooops! This category of products cannot be found.")
    if category and not category.is_leaf_node():
        template = loader.get_template('catalog/list.html')
        categories = category.get_descendants(include_self=True)
        context = {
            'categories': categories,
        }
        return HttpResponse(template.render(context, request))
        
    template = loader.get_template('catalog/product_list.html')
    products = None
    try:
        products = Product.objects.filter(category_id = category.id)
        context = {
            'category': category,
            'products': products,
        }
        return HttpResponse(template.render(context, request))
    except:
        context = {
            'category': category,
        }
        return HttpResponse(template.render(context, request))

def show_product(request, product_slug):
    product = None
    try:
        template = loader.get_template('catalog/product.html')
        product = Product.objects.get(slug=product_slug)
        context = {
            'product': product,
        }
        return HttpResponse(template.render(context, request))
    except:
        raise Http404("Ooops! This category cannot be found.")