from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class Home(View):
    def get(self, request):
        return HttpResponse("Devine Spa")

class About(View):
    def get(self, request):
        return HttpResponse("About Us")

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Service:
    def __init__(self, name, image, description, packagename1, packageprice1, packagename2, packageprice2, packagename3, packageprice3):
        self.name = name
        self.image = image
        self.description = description
        self.packagename1 = packagename1
        self.packageprice1 = packageprice1
        self.packagename2 = packagename2
        self.packageprice2 = packageprice2
        self.packagename3 = packagename3
        self.packageprice3 = packageprice3

services = [
    Service("Massage", "https://media.allure.com/photos/5ee11520a9ba330008e32528/4:3/w_2664,h_1998,c_limit/massage.jpg", "nice massage", "30 Minutes", "$40", "60minutes", "$50", "90 minutes", "$60")
]
       
class ServiceList(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = services
        return context


