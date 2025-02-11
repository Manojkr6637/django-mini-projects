from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User
# Create your models here.

class Payment(models.Model):
    
    #Enum data type
    
    PAYTMENT_TYPE = [
        ('OL', 'Online'),
        ('UPI', 'UPI'),
         ('OF', 'OFFLINE'),
        
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="payment/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=PAYTMENT_TYPE)
    description= models.TextField(default='')
    
    
    def __str__(self):
        return self.name
    
    
    
    #One to many
    
class PaymentReview(models.Model):
    payment =  models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='reviews')
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    rating = models.IntegerField()
    
    comment = models.TextField()
    
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
       return f'{self.user.username} review for {self.payment.name}'


# many to many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    payment_options = models.ManyToManyField(Payment, related_name='stores')
    
    def __str__(self):
        return self.name


#One to one

class PaymentCertificate(models.Model):
    
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, related_name='certificate')
    
    certificate_number= models.CharField(max_length=100)
    
    issued_date = models.DateTimeField(default=timezone.now)
    
    valid_until = models.DateTimeField()
    
    def __str__(self):
              return f'Certficate for {self.name.payment}' 