from rest_framework import generics
from rest_framework.response import Response
from .serializers import RegisterSerializer,UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token=super().get_token(user)
        token['username']=user.username
        token['first_name']=user.first_name
        token['email_address']=user.email
        
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

class RegisterAPIView(generics.GenericAPIView):
    serializer_class=RegisterSerializer
    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user=serializer.save()
        return Response(
            {
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "message":"User created successfully"
            }
        )
