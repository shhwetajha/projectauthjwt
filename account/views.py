from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import *
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
#Generate token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.

class UserRegisterationView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serial=UserRegisterationSerializer(data=request.data)
        if serial.is_valid(raise_exception=True):
            user=serial.save()
            token = get_tokens_for_user(user)
            return Response({"token":token,"msg":"registeration done successfullY!"},status=status.HTTP_200_OK)
        return Response({"msg":serial.errors},status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginView(APIView):
    def post(self,request,format=None):
        serial=UserLoginSerializer(data=request.data)
        if serial.is_valid(raise_exception=True):
            email=serial.data.get('email')
            password=serial.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login Success'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or password is not Valid']}},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'errors':serial.errors},status=status.HTTP_400_BAD_REQUEST)
        
# for the details of the user who has just logged in

class UserProfileView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        serial=UserProfileserializer(request.user)
        return Response(serial.data,status=status.HTTP_200_OK)
    

#User change
class UserChangePassword(APIView):
     permission_classes=[IsAuthenticated]
     def post(self,request,format=None):
         serializer=UserChangePasswordSerializer(data=request.data,context={'user':request.user})
         if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password changed successfully!!!'},status=status.HTTP_200_OK)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         


    



