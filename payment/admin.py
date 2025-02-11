from django.contrib import admin

from .models import Payment, PaymentReview, Store, PaymentCertificate

# Register your models here.

class PaymentReviewInline(admin.TabularInline):
    model = PaymentReview
    extra = 2


class PaymentOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    
    inlines = [PaymentReviewInline]
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('payment_options', )

class PaymentCertificateAdmin(admin.ModelAdmin):
    list_display = ('payment', 'certificate_number')
    
    
    
admin.site.register(Payment, PaymentOptionAdmin)
admin.site.register(Store, StoreAdmin)

admin.site.register(PaymentCertificate, PaymentCertificateAdmin)
