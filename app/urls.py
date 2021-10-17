from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import *


router = DefaultRouter()

router.register("pays", PaysApiView, basename="pays")
router.register("province", ProvinceApiView, basename="province")
router.register("ville", VilleApiView, basename="ville")
router.register("type", TypeApiView, basename="type")
router.register("lieu", LieuApiView, basename="lieu")
router.register("evenement", EvenementApiView, basename="evenement")


urlpatterns = [
    path('', include(router.urls)),
]
