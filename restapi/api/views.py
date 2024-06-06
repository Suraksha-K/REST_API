from django.shortcuts import render
from .serializers import UserRegister
from rest_framework.views import APIView 
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class register(APIView):
    def post(self,request,format=None):
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='User Registered Successfully!'
            data['username']=account.username
            data['email']=account.email
           
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)

class home(APIView):
    permission_classes =(IsAuthenticated,)
    
    def get(self,request):
        content={}
        
        content={'user':str(request.user),'userid':str(request.user.id)}
        content['response']='Login Successfull'
        return Response(content)

class welcome(APIView):
    permission_classes =(IsAuthenticated,)
    
    def get(self,request):
        content={}
        
        content={'user':str(request.user),'userid':str(request.user.id)}
        content['response']='Login Successfull'
        return Response(content)

