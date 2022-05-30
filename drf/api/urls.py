from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from api.views import UserListAPI, RegisterAPI, LoginAPI, MyTokenObtainPairView, MyTokenRefreshView, LogoutView

app_name='api'
urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',MyTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/logout/', LogoutView.as_view(), name='logoout'),
    
    path('user/', UserListAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
]
