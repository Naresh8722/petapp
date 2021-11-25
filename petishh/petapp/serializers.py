
from django.db.models import fields
from django.db.models.base import Model
from .models import Product, Category
from rest_framework import serializers

from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        Model=Category
        fields='__all__'



import base64
from os import write

from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework.exceptions import AuthenticationFailed
# from sellerMenu.serializers import SellerCategoryDetailsSerializer
# from django.contrib.auth.models import Group, GroupManager
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator, default_token_generator
from django.conf import settings
# from rest_framework import serializers
from rest_framework.authtoken.models import Token
from petapp.models import Users,EmailCodeVerification,Profileinfo


User = get_user_model()

# //////////////////////////// Customer login reg ///////////////////////////////
class CustomerSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, allow_blank=False, max_length=200)
    phone_no = serializers.CharField(required=True, allow_blank=False, max_length=20)
    email = serializers.CharField(required=True, allow_blank=False, max_length=200)
    

    class Meta:
        model =get_user_model()
        fields = ['id','email', 'phone_no', 'password','username','first_name', 'last_name']

class CustomerLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True, write_only=True)
    email = serializers.CharField(required=False, write_only=True, label="Email Address")
    phone_no = serializers.CharField(required=False, write_only=True, max_length=10, label="Mobile Number")
    token = serializers.CharField(allow_blank=True, read_only=True)
    password = serializers.CharField(required=True, write_only=True, style={'password':'password'})

    class Meta(object):
        many = True
        model = Users
        fields = ['id','email','phone_no', 'username','password', 'token', 'is_superuser', 'is_active', 'is_staff', 'last_login']

# /////////////////////////////////////////////////LoginSerializer//////////////////////////////////////////////////////////

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True, write_only=True)
    email = serializers.EmailField(required=True, write_only=True, label="Email Address")
    phone_no = serializers.CharField(required=True, write_only=True, max_length=10, label="Mobile Number")
    token = serializers.CharField(allow_blank=True, read_only=True)
    password = serializers.CharField(required=True, write_only=True, style={'input_type': 'password'})

    class Meta(object):
        many = True
        model = Users
        fields = ['id', 'phone_no', 'email', 'username', 'password', 'token', 'first_name', 'last_name', 'email',
                  'is_superuser', 'is_active', 'is_staff', 'last_login']


# /////////////////////////////////////////////////////ProfileSerializer//////////////////////////////////////////////////////


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'phone_no', 'first_name', 'last_name','profile_image']                  





class EmailViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCodeVerification
        fields ="__all__"
