from .models import User
from .serializers import UserListSerializer, UserCreateSerializer, UserDitailSerializer
from apps.viewsets import CustomModelViewSet


class UserViewSet(CustomModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDitailSerializer
        if self.action == 'create':
            return UserCreateSerializer
        else:
            return self.serializer_class
