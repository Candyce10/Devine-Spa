from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about_us/', views.About.as_view(), name="about"),
    path('services/', views.ServiceList.as_view(), name="service_list"),
    path('services/<int:pk>/', views.ServiceDetail.as_view(), name="service_detail"),
    path('reviews/', views.ReviewList.as_view(), name="review_list"),
    path('reviews/new', views.ReviewCreate.as_view(), name="review_create"),
    path('book_appointment/', views.AppointmentCreate.as_view(), name="appointment"),
    path('book_appointment/confirmation/', views.ConfirmationPage.as_view(), name="confirmation"),

]