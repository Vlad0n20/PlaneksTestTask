from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SchemaViewSet

app_name = 'schema'

router = DefaultRouter()

router.register(r'schemas', SchemaViewSet)

urlpatterns = [
    path('', include(router.urls))
]
