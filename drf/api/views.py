from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpRequest, JsonResponse, HttpResponse

from django.contrib.auth.models import User

from mysite.serializers import UserSerializer

class UserListAPI(APIView):
    def get(self, request: HttpRequest, *args, **kwargs):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class RegisterAPI(APIView):
    def post(self, request: HttpRequest, *args, **kwargs):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                print(status.HTTP_201_CREATED)
                return HttpResponse(status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)