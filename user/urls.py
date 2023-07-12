
from django.urls import include, path
from .views import ApplicantViewSet
from rest_framework.routers import DefaultRouter
# Create a router and register the ApplicantViewSet
router = DefaultRouter()
router.register(r'register', ApplicantViewSet)


urlpatterns = [path('', include(router.urls)),]