from rest_framework import serializers
from account.models import User



class UserRegisterationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['email','name','password','password2','tc']
        extra_kwargs={'password':{'write_only':True}}


#validating password and confirm password
    def validate(self,attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password!= password2:
            raise serializers.ValidationError("Password and confirm password do not match")
        return attrs

#here we are creating user and we have custom user
    def create(self,validate_data):
        return User.objects.create_user(**validate_data)
    

#creating Login Serializer
class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email','password']


#creating user profile serializer
class UserProfileserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','id']

#creating change-password serializer:
class UserChangePasswordSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    password2=serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields=['password','password2']

    def validate(self,attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        user=self.context.get('user')
        if password!= password2:
            raise serializers.ValidationError("Password and confirm password do not match")
        user.set_password(password)
        user.save()
        return attrs
    


    










