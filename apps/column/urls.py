from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ColumnViewSet

app_name = 'column'

router = DefaultRouter()

router.register(r'columns', ColumnViewSet)

urlpatterns = [
    path('', include(router.urls))
]
