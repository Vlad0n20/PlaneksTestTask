from rest_framework import serializers

from .models import Column
from apps.schema.serializers import SchemaListSerializer


class ColumnListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['id', 'name', 'type']


class ColumnCreateSerializer(serializers.ModelSerializer):
    schema_id = serializers.IntegerField(allow_null=False)

    class Meta:
        model = Column
        fields = ['id', 'name', 'type', 'params', 'schema_id']


class ColumnDitailSerializer(serializers.ModelSerializer):
    schema = SchemaListSerializer()

    class Meta:
        model = Column
        fields = ['id', 'name', 'type', 'params', 'schema']
