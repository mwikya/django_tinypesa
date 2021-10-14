from django.contrib import admin
from tinypesa.models import TinyPesaPayment

# Register your models here.


class TinyPesaPaymentAdmin(admin.ModelAdmin):
    '''
        Admin View for TinyPesaPayment
    '''
    list_display = ("reference", "amount", "msisdn", "payment_date",
                    "mpesa_transaction_id", "status")
    # readonly_fields = ("mpesa_transaction_id", "tiny_pesa_id")
    list_filter = ("status", )


admin.site.register(TinyPesaPayment, TinyPesaPaymentAdmin)
