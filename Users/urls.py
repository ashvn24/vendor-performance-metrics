from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import *

urlpatterns = [
    path('token/refresh',TokenRefreshView.as_view(),name= 'token_refresh'),
    path('user/reg/', UserRegAPIView.as_view()),
    path('user/log/', LoginAPIView.as_view()),
]