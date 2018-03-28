from django.contrib.auth.models import User
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import PasswordResetSerializer
from rest_framework import serializers,exceptions
from django.shortcuts import get_object_or_404
from .forms import CustomPasswordResetForm
from django.utils.translation import ugettext_lazy as _
from allauth.account.adapter import get_adapter
from allauth.account import app_settings as allauth_settings
from allauth.utils import (email_address_exists,
get_username_max_length)

from apps.users.models import UserProfile

class PasswordResetSerializerFix(PasswordResetSerializer):
    password_reset_form_class = CustomPasswordResetForm

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id",)

class UserDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    userprofile = UserProfileSerializer()

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'full_name', 'email','last_login', 'is_active',
                  'date_joined','userprofile',)

class UserDetailRestKnoxFix(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    userprofile = UserProfileSerializer()

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'full_name', 'email', 'last_login', 'is_active',
                  'date_joined','userprofile')


class RegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username')

    def custom_signup(self, request,user):
        data = self.validated_data
        UserProfile.objects.create(user=user)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['username'] = data.get('email')
        data['first_name'] = self.validated_data.get('first_name')
        data['last_name'] = self.validated_data.get('last_name')
        return data