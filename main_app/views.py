from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Service, Review, Appointment, ServiceDetails
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .forms import ReviewForm, AppointmentForm

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


class ConfirmationPage(TemplateView):
    template_name = "confirmation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["appointments"] = Appointment.objects.all()
        return context


class ReviewList(TemplateView):
    template_name = "reviews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.all()
        return context


class ReviewCreate(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "review_create.html"
    success_url = "/reviews/"
  


class AppointmentCreate(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = "appointment_create.html"
    success_url = "/confirmation/"


