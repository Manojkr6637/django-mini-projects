from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Payment

def payment(request):
   # return HttpResponse("Home page")
   payments = Payment.objects.all()
   
   return render(request, 'payment/payment.html', {"payments":payments})
 
def payment_detail(request, payment_id):   
    payment = get_object_or_404(Payment, pk=payment_id)    
    return render(request, 'payment/payment_detail.html', {'payment': payment})