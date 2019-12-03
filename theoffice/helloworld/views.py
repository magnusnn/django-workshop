from django.shortcuts import render, HttpResponse
from django.views import generic


def http_index(request):
    return HttpResponse('Hello world!')

def render_index(request):
    return render(request, 'helloworld/index.html', {})

class HelloWorldView(generic.TemplateView):
    template_name = 'helloworld/index.html'