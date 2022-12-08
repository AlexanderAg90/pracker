from django.http import HttpResponse
from django.template import loader

def index(reqest):
    template = loader.get_template('site_main.html')
    return HttpResponse(template.render())