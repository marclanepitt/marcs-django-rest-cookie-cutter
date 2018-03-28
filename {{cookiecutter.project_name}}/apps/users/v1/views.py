from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from knox.auth import TokenAuthentication
from knox.views import LoginView
from knox.models import AuthToken
from django.contrib.auth.signals import user_logged_in, user_logged_out
from knox.settings import knox_settings
from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated
from rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from rest_framework import status
from rest_auth.views import PasswordResetView
import json
from rest_framework import permissions
from . import serializers
from ..models import UserProfile

# {
# "auth":{"username":"q@q.com","password":"qqqqqqqq"}
# }

class PasswordResetFixView(PasswordResetView):
    serializer_class = serializers.PasswordResetSerializerFix

class KnoxLoginView(LoginView):
    def post(self, request, format=None):
        token = AuthToken.objects.create(request.user)
        user_logged_in.send(sender=request.user.__class__, request=request, user=request.user)
        UserSerializer = knox_settings.USER_SERIALIZER
        user_corrected_data = UserSerializer(request.user).data
        return Response({
            'user': user_corrected_data,
            'token':token
        })

class UserDetailView(generics.RetrieveAPIView):

    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = serializers.UserDetailSerializer

    def get_object(self):
        if self.kwargs.get('pk', None) == 'me':
            return get_object_or_404(User, pk=self.request.user.id)
        return super().get_object()


class UserProfileCreateView(generics.CreateAPIView):
    serializer_class = serializers.UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserProfileListView(generics.ListAPIView):
    serializer_class = serializers.UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class RegistrationView(RegisterView):
    def get_response_data(self, user):
        token = AuthToken.objects.create(user)
        UserSerializer = knox_settings.USER_SERIALIZER
        user_corrected_data = UserSerializer(user).data
        user_corrected_data['token'] = token
        return user_corrected_data