from django.conf.urls import include, url
from rest_framework import routers

from .views import TxtViewSet

router = routers.DefaultRouter()
router.register('', TxtViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
