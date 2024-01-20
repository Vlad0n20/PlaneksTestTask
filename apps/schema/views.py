from apps.viewsets import CustomModelViewSet

from .models import Schema
from .serializers import SchemaListSerializer, SchemaDitailSerializer


class SchemaViewSet(CustomModelViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemaListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SchemaDitailSerializer
        else:
            return self.serializer_class
