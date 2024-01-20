from rest_framework import serializers

from .models import Schema
from apps.user.serializers import UserListSerializer


class SchemaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema
        fields = ['name', 'number_of_records']


class SchemaDitailSerializer(serializers.ModelSerializer):
    user = UserListSerializer()

    class Meta:
        model = Schema
        fields = ['name', 'number_of_records', 'user']
