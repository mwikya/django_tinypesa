import uuid
from django.db import models
# Create your models here.
STATUSES = [
    (0, "Successful"),
    (1, "Failed"),
]


class AbstractTinyPesaPayment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reference = models.CharField(null=True, max_length=50)
    amount = models.FloatField(null=True)
    msisdn = models.CharField(null=True, max_length=50)
    mpesa_transaction_id = models.CharField(null=True, max_length=50)
    tiny_pesa_id = models.UUIDField(null=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, choices=STATUSES)

    class Meta:
        abstract = True
        ordering = ['payment_date']


class TinyPesaPayment(AbstractTinyPesaPayment):

    class Meta:
        swappable = 'TINYPESA_PAYMENT_MODEL'

    def __str__(self):
        return self.mpesa_transaction_id
