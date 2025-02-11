from django import forms


from .models import Payment


class PaymentForm(forms.Form):
    payment_option = forms.ModelChoiceField(queryset=Payment.objects.all(), label="Select payment options")
    #  payment_option = forms.CharField()
    
    
    