from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Service, Review, Appointment, ServiceDetails
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .forms import ReviewForm

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
    template_name = "service_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service_detail"] = ServiceDetails.objects.all()
        return context
        

class AppointmentPage(View):
     def get(self, request):
        return HttpResponse("Book Appointment")

class AppointmentPage(TemplateView):
    template_name = "appointment.html"
    

class AppointmentCreate(View):
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        date = request.POST.get("date")
        appointment = Appointment.objects.create(name=name, email=email, number=number, date=date)
        appointment.save()
        return HttpResponseRedirect('confirmation')




class ConfirmationPage(TemplateView):
    template_name = "confirmation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.request.GET.get("id")
        if id != None:
            context["appointment"] = Appointment.objects.filter(name__icontains=id)
        else:
            context["appointment"] = Appointment.objects.all()
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
  



