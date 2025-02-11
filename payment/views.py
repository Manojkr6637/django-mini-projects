from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Payment, Store

from .forms import PaymentForm

#Create your view here


def payment(request):
   # return HttpResponse("Home page")
   payments = Payment.objects.all()
   
   return render(request, 'payment/payment.html', {"payments":payments})
 
def payment_detail(request, payment_id):   
    payment = get_object_or_404(Payment, pk=payment_id)    
    return render(request, 'payment/payment_detail.html', {'payment': payment})
 
 
def payment_store_view(request):
   stores = None
   if request.method == 'POST':
     form = PaymentForm(request.POST)
     if form.is_valid():   
      payment_option = form.cleaned_data['payment_option']
      stores = Store.objects.filter(payment_options = payment_option)
   else:
      form = PaymentForm()
           
   return render(request, 'payment/store.html', {"stores": stores, 'form':form}) 
 