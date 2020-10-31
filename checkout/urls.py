from django.urls import path
from . import views

app_name = 'checkout'
urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('payment_successful/', views.payment_successful, name='payment_successful')
]
