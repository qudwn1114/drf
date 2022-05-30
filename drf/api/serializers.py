from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer, TokenVerifySerializer
from rest_framework_simplejwt.state import token_backend
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from django.contrib.auth.models import User, update_last_login
from datetime import datetime

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = serializers.CharField()
    access = serializers.CharField(read_only=True)
    token_class = RefreshToken

    def validate(self, attrs):
            verify_refresh(self.token_class(attrs["refresh"]))
            data = super(MyTokenRefreshSerializer, self).validate(attrs)
            decoded_payload = token_backend.decode(data['refresh'], verify=True)
            user_uid=decoded_payload['user_id']
            jti=decoded_payload['jti']
            exp=decoded_payload['exp']
            OutstandingToken.objects.create(
                user=User.objects.get(pk=user_uid),
                jti=jti,
                expires_at = datetime.fromtimestamp(exp),
                token = str(data['refresh']),
                created_at=datetime.utcnow(),
            )

            return data

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = '__all__' 


def verify_refresh(refresh_token):
    try:
        token = OutstandingToken.objects.get(token=str(refresh_token))
    except OutstandingToken.DoesNotExist:
        raise serializers.ValidationError("Invalid Token")

    return token

