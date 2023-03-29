from django.urls import path
from .views import *

urlpatterns=[
    path('quotes/',QuoteListAPIView.as_view(),name="quotes")
]