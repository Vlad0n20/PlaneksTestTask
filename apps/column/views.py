from apps.viewsets import CustomModelViewSet

from .models import Column
from .serializers import ColumnDitailSerializer, ColumnCreateSerializer, ColumnListSerializer


class ColumnViewSet(CustomModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnDitailSerializer

    def get_serializer_class(self):
        if self.action == ['create', 'update', 'partial_update']:
            return ColumnCreateSerializer
        elif self.action == 'retrieve':
            return ColumnDitailSerializer
        else:
            return self.serializer_class
