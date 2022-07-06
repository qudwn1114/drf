from django.urls import path, include
from mysite.views import IndexView
app_name='mysite'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
