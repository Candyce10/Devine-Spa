from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about_us/', views.About.as_view(), name="about"),
    path('services/', views.ServiceList.as_view(), name="service_list")

]