from django.urls import path
from .views import *

urlpatterns=[
    path('quotes/',QuoteListAPIView.as_view(),name="quotes"),
    path('quotes/<int:id>',QuoteListAPIView.as_view(),name="quote"),
    path('contacts/',ContactListAPIView.as_view(),name="contacts"),
    path('contacts/<int:id>',ContactListAPIView.as_view(),name="contact"),
]