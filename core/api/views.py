from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from core.models import *
from .serializers import QuoteSerializer

class QuoteListAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        quotes=Quotes.objects.all()
        serializer=QuoteSerializer(quotes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data={
            'name':request.data.get('name'),
            'phone':request.data.get('phone'),
            'email':request.data.get('email'),
            'address':request.data.get('address'),
            'zip_code':request.data.get('zip_code'),
        }
        serializer=QuoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
