from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from core.models import *
from .serializers import QuoteSerializer,ContactSerializer
from django.shortcuts import get_object_or_404

class QuoteListAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request, id=None, *args, **kwargs):#127.0.0.1:8000/quotes
        if id:
            quote=Quotes.objects.get(id=id)
            serializer=QuoteSerializer(quote)
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
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
    
    def put(self,request,  id=None, *args, **kwargs):
        if id:
            quote=Quotes.objects.get(id=id)
        quote_serializer=QuoteSerializer(data=request.data,instance=quote)
        if quote_serializer.is_valid():
            quote_serializer.save()
            return Response(QuoteSerializer(quote).data)
        return Response(quote_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, id=None, *args, **kwargs):
        quote=get_object_or_404(Quotes,id=id)
        quote.delete()
        return Response({"status":"success","data":"Item deleted!"})



class ContactListAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request, id=None, *args, **kwargs):#127.0.0.1:8000/quotes
        if id:
            contact=Contact.objects.get(id=id)
            serializer=ContactSerializer(contact)
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        contacts=Contact.objects.all()
        serializer=ContactSerializer(contacts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data={
            'first_name':request.data.get('first_name'),
            'last_name':request.data.get('last_name'),
            'phone':request.data.get('phone'),
            'email':request.data.get('email'),
            'message':request.data.get('message'),
        }
        serializer=ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,  id=None, *args, **kwargs):
        if id:
            contact=Contact.objects.get(id=id)
        contact_serializer=ContactSerializer(data=request.data,instance=contact)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return Response(ContactSerializer(contact).data)
        return Response(contact_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, id=None, *args, **kwargs):
        contact=get_object_or_404(Contact,id=id)
        contact.delete()
        return Response({"status":"success","data":"Item deleted!"})
