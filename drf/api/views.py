from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken

from django.http import HttpRequest, JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth import get_user

from api.serializers import UserSerializer, MyTokenObtainPairSerializer, MyTokenRefreshSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

class MyTokenRefreshView(TokenRefreshView):
    serializer_class=MyTokenRefreshSerializer

class UserListAPI(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request: HttpRequest, *args, **kwargs):
        print(get_user(request))
        print(timedelta(days = 0, hours=9 + 0, minutes=1))
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class RegisterAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request: HttpRequest, *args, **kwargs):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                print(status.HTTP_201_CREATED)
                return HttpResponse(status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request: HttpRequest, *args, **kwargs):
            try:
                id = request.data['username']
                password = request.data['password']
                user = authenticate(username=id, password=password)
                if user is not None:
                    login(request, user)
                else:
                    return JsonResponse({
                            "error": "로그인정보오류"
                        }, status=status.HTTP_400_BAD_REQUEST
                    )
                return JsonResponse({
                    "url" : "abc"
                }, status=status.HTTP_201_CREATED)
            except:
                return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
