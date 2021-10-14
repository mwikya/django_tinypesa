from rest_framework import routers
from tinypesa.viewsets import TinyPesaViewset


router = routers.DefaultRouter()
router.register(r'', TinyPesaViewset, "process")
