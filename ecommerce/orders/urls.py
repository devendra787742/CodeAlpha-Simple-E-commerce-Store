from django.urls import path
from . import views

urlpatterns = [
    path('place/', views.place_order, name='place_order'),
    path('history/', views.order_history, name='order_history'),
    path('payment/<int:order_id>/', views.payment_page, name='payment'),
    path('payment-success/<int:order_id>/', views.payment_success, name='payment_success'),
]
