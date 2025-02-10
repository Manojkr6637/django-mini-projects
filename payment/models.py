from django.db import models

from django.utils import timezone
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
    