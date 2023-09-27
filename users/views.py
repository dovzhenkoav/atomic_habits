from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = UserSerializer

    def perform_create(self, serializer):  #
        new_user = serializer.save()
        new_user.set_password(self.request.data['password'])
        new_user.save()
