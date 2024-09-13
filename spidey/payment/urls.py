from django.urls import path
from . import views

urlpatterns = [
    path('payment/<int:pk>/', views.payment_view, name='payment'),
    path('payment/success/', views.payment_success_view, name='payment_success'),
]