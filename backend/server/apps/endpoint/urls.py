from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.endpoint.views import EndpointViewSet
from apps.endpoint.views import MLAlgorithmViewSet
from apps.endpoint.views import MLAlgorithmStatusViewSet
from apps.endpoint.views import MLRequestViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    url(r"^api/v1/", include(router.urls)),
]