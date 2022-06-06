from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse
from .models import Service, Review
from django.views.generic.base import TemplateView
from django.views.generic import DetailView

class Home(View):
    def get(self, request):
        return HttpResponse("Divine Spa")

class About(View):
    def get(self, request):
        return HttpResponse("About Us")

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"


class ServiceList(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        return context
        
class ServiceDetail(DetailView):
    model = Service
    template_name = "service_detail.html"

class ReviewCreate(View):
    
    def post(self, request, pk):
        name = request.POST.get("name")
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        service = Service.objects.get(pk=pk)
        Review.objects.create(name=name, rating=rating, comment=comment, service=service)
        return redirect('artist_detail', pk=pk)


   
