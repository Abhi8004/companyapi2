from rest_framework import serializers
from testapp.models import User,UserManager

class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model=User
        fields=['email', 'name', 'password', 'password2']
        extra_kwargs={'password':{'write_only':True}}

    #Validating Password & Confirm Password While Registration
    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password does not match")
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email', 'password']
