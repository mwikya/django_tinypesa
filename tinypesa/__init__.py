from django.conf import settings
from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured


def get_tinypesa_payment_model():
    """
    Return the TinyPesaPayment model that is active in this project.
    """
    try:
        return django_apps.get_model(settings.TINYPESA_PAYMENT_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured(
            "TINYPESA_PAYMENT_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "TINYPESA_PAYMENT_MODEL refers to model '%s' that has not been installed" % settings.TINYPESA_PAYMENT_MODEL
        )
