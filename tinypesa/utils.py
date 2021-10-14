import requests
from django.conf import settings


HEADERS = {
    'Accept': 'application/json',
    'Apikey': settings.TINYPESA_SETTINGS['APIKEY'],
    'Content-Type': "application/json"
}


def stk_push(amount, msisdn, account_no):
    data = {
        "amount": amount,
        "msisdn": msisdn,
        "account_no": account_no
    }
    res = requests.post(settings.TINYPESA_SETTINGS["INITIALIZE_URL"],
                        json=data, headers=HEADERS)
    return res


amount = 20
msisdn = "0708300418"
account_no = "ONIYOU2XXYI0"
