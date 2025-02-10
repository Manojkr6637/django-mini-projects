from django.urls import path

from . import views

#http:localhost:8000/payment/order

urlpatterns = [ 
    path('', views.payment, name='payment'),    
    path('<int:payment_id>/', views.payment_detail, name='payment_detail')
    
]