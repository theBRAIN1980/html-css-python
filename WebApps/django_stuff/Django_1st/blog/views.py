from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

def about(request):
    return HttpResponse("<h1> About me! </h1>")

def add(request):
    a = int(request.GET.get("a"))
    b = int(request.GET.get("b"))
    return HttpResponse(f"Suma este {a+b}")

def mul(request, a, b, c):
    return HttpResponse(f"<h1>Produsul este {a*b*c}</h1>")


# Create your views here.
class SinglePage(TemplateView):
    template_name = "singlepost.html"

class BlogPage(TemplateView):
    template_name = "blog.html"

class AboutPage(TemplateView):
    template_name = "about.html"

class ContactPage(TemplateView):
    template_name = "contact.html"

class IndexPage(TemplateView):
    template_name = "index.html"

class Proj1Page(TemplateView):
    template_name = "proj1.html"

class ProjectsPage(TemplateView):
    template_name = "projects.html"

def welcome(request):
    return render(request, "home.html")

def hello_nume(request, nume):
    return render(request, "base.html", {'username': nume})

class SalutPage(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, *args, **kwargs):
        context = {'username': kwargs['name']}
        return context

