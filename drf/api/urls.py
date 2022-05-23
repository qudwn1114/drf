from django.urls import path, include
from api.views import UserListAPI, RegisterAPI

app_name='api'
urlpatterns = [
    path('user/', UserListAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
]
