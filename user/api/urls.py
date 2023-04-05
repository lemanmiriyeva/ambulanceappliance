from django.urls import path
from .views import MyTokenObtainPairView,RegisterAPIView

urlpatterns=[
    path('login/',MyTokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('register/',RegisterAPIView.as_view(),name="register")
]