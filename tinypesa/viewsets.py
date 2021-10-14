from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from tinypesa.models import TinyPesaPayment


class TinyPesaViewset(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]

    @action(detail=False, methods=['post'])
    def process(self, request, *args, **kwargs):
        data = request.data['Body']['stkCallback']
        item = data["CallbackMetadata"]["Item"]
        transaction_id = ""
        for obj in item:
            if obj["Name"] == "MpesaReceiptNumber":
                transaction_id = obj["Value"]
        code = 0 if data["ResultCode"] == 0 else 1
        TinyPesaPayment.objects.create(
            status=code,
            msisdn=data["Msisdn"],
            amount=data["Amount"],
            reference=data["ExternalReference"],
            mpesa_transaction_id=transaction_id,
            tiny_pesa_id=data["TinyPesaID"],
        )
        return Response({"message": "Ok."}, 200)
