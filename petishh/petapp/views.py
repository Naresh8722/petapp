from django.shortcuts import render
from rest_framework import serializers
from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from django.http import HttpResponse
from petapp.serializers import *
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


from .models import Product
from .serializers import ProductSerializer
# Create your views here.
from .models import Category, Product
def categories(request):
    return {'categories': Category.objects.all()}
    
   


class ProductView(generics.ListAPIView):
    queryset =Product.objects.all()
    serializer_class = ProductSerializer

    def all_products(request):
        """
        List all code products, or create a new Product.
        """
        if request.method == 'GET':
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ProductSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)



    def product_detail(request, pk):    
        """
        Retrieve, update or delete a code Product.
        """
        try:
            products = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = ProductSerializer(products)
            return JsonResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ProductSerializer(products, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            Product.delete()
            return HttpResponse(status=204)




from django.db.models.query import QuerySet

from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from django.http import HttpResponse
from .serializers import *
from django.utils import timezone
import base64
from slugify import slugify
import random
from django.db.models import Q
from rest_framework.views import APIView
import math, random
from twilio.rest import Client
import json
import requests
import smtplib,ssl

def dashboard(request):
    return render(request, 'petapp/dashboard.html')

class JSONResponse(HttpResponse):
    """ An HttpResponse that renders its content into JSON. """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# ////////////////////////////  CUSTOMER REG LOGIN //////////////////////////////////////////////


class CustomerRegistrationView(generics.ListAPIView):
    queryset =User.objects.all()
    serializer_class = CustomerSignupSerializer
    def post(self, request):
        serializer = CustomerSignupSerializer(data=request.data)
        if serializer.is_valid():           
            print("started validation")
            requestData = serializer.validated_data
            print(requestData)
            email = requestData['email']
            password = requestData['password']
            phone_no = requestData['phone_no']
            referelcode ='home'+str(random.randint(10000000, 99999999))
            wallet=0
            p_d=password
            account = account_encoder(p_d)
            username = email.split("@")[0]

            ## check Email aiiready exist or not
            user = Users.objects.filter(email=email,is_deleted=False,user_type=1).count()            
            user_no = Users.objects.filter(phone_no=phone_no, is_deleted=False,user_type=1).count()
            usernm = Users.objects.filter(username=username,is_deleted=False,user_type=1).count()  
            print("=================",user,usernm,user_no)
            if usernm>0:
                username=username+str(random.randint(1000, 9999))
            if user > 0:
                msg = {"Unauthorized error ": ['Email already Registered....', ]}
                errors = {'errors': msg}
                return JSONResponse(errors, status=401)
            elif user_no >0:
                msg = {"Unauthorized error ": ['Mobile Already Registered....', ]}
                errors = {'errors': msg}
                return JSONResponse(errors, status=401)
            else:
                obj = Users.objects.create_user( 
                    email=email,
                    phone_no=phone_no,
                    username=username,
                    account=account,
                    referelcode = referelcode,
                    wallet=wallet,
                    is_staff=False,
                    is_superuser=False,
                    is_phone_verified=False,
                    is_email_verified=False,
                    is_active=True,
                    user_type=1
                )
                obj.set_password(password)
                obj.save()
                data = {
                    'status': 1,
                    'id': obj.id,
                    'email': obj.email,
                    'username': obj.username,
                    'message': 'Customer created successfully'
                }
                return JSONResponse(data, status=200)
        else:
            return JsonResponse({'msg': 'Email Or Password did not match'}, status=400)


class CustomerLoginView(generics.ListAPIView):
    queryset =User.objects.all()
    serializer_class = CustomerLoginSerializer                 
    def post(self, request):
        serializer = CustomerLoginSerializer(data=request.data)
        if serializer.is_valid():
            mobile = request.data['phone_no']
            email = request.data['email']
            password = request.data['password']
            User = get_user_model()
            #user = User.objects.filter((Q(email=email)|Q(phone_no=mobile)),user_type=1, is_deleted=False, is_blocked=False).first()
            user = User.objects.filter(email=email,user_type=1, is_deleted=False, is_blocked=False).first()
            if user:
                if user.check_password(password):  ## Check password matched or not
                    if user.is_phone_verified:
                        if user.is_email_verified:  ## Check user phone is verified or not
                            if user.is_active:  ## Check user active or deactive
                                token, created = Token.objects.get_or_create(
                                    user=user)  ### Get user authentication token
                                token_data = token.key  ### if it is first login then create token first and get token
                                user.last_login = timezone.now()
                                user.save()
                                serialize_userdata = {
                                    'status': 1,
                                    'id': user.id,
                                    'email': user.email,
                                    'phone_no':user.phone_no,
                                    'username': user.username,
                                    'token': token_data,
                                    'first_name': user.first_name,
                                    'last_name': user.last_name,
                                    'is_superuser': user.is_superuser,
                                    'is_active': user.is_active,
                                    'is_staff': user.is_staff,
                                    'last_login': user.last_login
                                }
                                #return JSONResponse(serialize_userdata, status=200)
                                return JSONResponse({'status': 0, 'msg': 'Login Successfull'}, status=200)
                            else:
                                return JSONResponse({'status': 0, 'msg': 'Your account is not activated.'}, status=200)
                        else:
                            return JsonResponse({'status': 4, 'msg': 'Email is not verified',"email":user.email}, status=202)
                    else:
                        if user.is_email_verified:
                            return JsonResponse({'status': 2, 'msg': 'Your Mobile Number is not verified'}, status=202)
                        else:
                            return JsonResponse({'status': 3, 'msg': 'Your Mobile Number & email is not verified',"email":user.email}, status=202)
                else:
                    return JsonResponse({'status': 0, 'msg': 'Password did not match'}, status=200)
            else:
                return JsonResponse({'status': 0, 'msg': 'Mobile Number did not match'}, status=200)
            
        else:
            return JsonResponse({'msg': 'Mobile Or Password did not match serializer'}, status=401)





def account_encoder(account):
    account_string_bytes = account.encode("ascii")
    base64_bytes = base64.b64encode(account_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return  base64_string


def account_decoder(account):
    account_string_bytes = account.encode("ascii")
    base64_bytes = base64.b64decode(account_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string    


# ////////////////////////////  CUSTOMER LOGIN //////////////////////////////////////////////
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *
import os
from base64 import urlsafe_b64decode
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import smart_str, smart_bytes, force_str
from rest_framework.response import Response
class CustomerProfileView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    # Get All Profile Information
    queryset =Users.objects.all()
    serializer_class = CustomerProfileSerializer 
    def get(self, request, format=None):
        user = request.user
        user_id = user.id
        response_data = {}
        profile_image_name = ''
        rs = User.objects.filter(
            id=user_id, user_type=1, is_active=True, is_blocked=False, is_deleted=False)
        if rs:
            user_serialize = CustomerProfileSerializer(rs, many=True)
            for details in user_serialize.data:
                profile_image_name = details['profile_image']
                if profile_image_name is not None:
                    if os.path.exists('media/profile_image/' + profile_image_name):
                        base64_image = encode_image_base64(
                            settings.MEDIA_ROOT + '/profile_image/' + profile_image_name)
                        details['profile_image'] = base64_image
            response_data['status'] = 1
            response_data['msg'] = 'Successfully get seller details'
            response_data['profile_details'] = user_serialize.data
            http_status_code = 200
        else:
            response_data['status'] = 0
            response_data['msg'] = 'No data found'
            response_data['profile_details'] = []
            http_status_code = 404
        return Response(response_data, status=http_status_code)

# For edit profile
    def post(self, request, format=None):
        response_data = {}
        user = request.user
        user_id = user.id
        rs = User.objects.filter(
            id=user_id, user_type=1, is_active=True, is_blocked=False, is_deleted=False).first()
        if rs:
            obj = User.objects.filter(id=user_id).update(
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
            )
            response_data['status'] = 1
            response_data['massage'] = "User update successfully"
            response_data['user_id'] = user_id
            return Response(response_data, status=200)
        else:
            response_data['status'] = 0
            response_data['massage'] = "User not found"
            response_data['user_id'] = user_id
            return Response(response_data, status=200)    





import smtplib,ssl
from email.message import EmailMessage


class EmailDetailsViewCustomer(APIView):
    def post(self, request, *args, **kwargs):
        response_data = request.data
        email = request.data.get('email')
        response = {}
        rs = User.objects.filter(email=email,is_blocked=False,user_type=1,is_deleted=False)
        if rs:
            for i in rs:
                user_id=i.id
            otp = generateEmail_otp(email)
            message =send_mail_otp(otp,email)
            if message:
                save_db={}
                save_db['created_date'] = timezone.now()
                # if email != user.email:
                #     try:
                #         subject = 'Request for adding a category/product'
                #         message = 'I am requestion for approval of adding a new oroduct/category'
                #         recepient = str(sub['Email'].value())
                #         send_mail(subject, 
                #             message, user.email, [], fail_silently = False)
                #         return JsonResponse({'status': 1, 'msg': 'Email sent successfully'}, status=200)
                    # except:
                save_db['email'] = email
                save_db['verification_code'] = otp
                save_db['user']=user_id
                save_db['modified_date'] = timezone.now()
                serializer = EmailViewSerializer(data=save_db)
                if serializer.is_valid():
                    user = EmailCodeVerification.objects.filter(user_id=user_id,is_deleted=False).first()
                    if not user:
                        serializer.save()
                        response['status'] = 1
                        response['msg'] = 'OTP Sent'
                        http_status_code = 200
                    else:
                        EmailCodeVerification.objects.filter(user_id=user_id).update(verification_code=otp)
                        response['status'] = 1
                        response['msg'] = 'OTP Sent'
                        http_status_code = 200
                else:
                    response['status'] = 0
                    http_status_code = 404
            else:
                response['status'] = 0
                response['msg'] = 'OTP cannot be sent!!'
                http_status_code = 404

        else:
            response['status'] = 0
            response['msg'] = 'No user found'
            http_status_code = 404
        print(response)
        return Response(response, status=http_status_code)




def sendsms(number, msg):
    payload = {
        'sender_id': 'FSTSMS',
        'message': "Your Otp for Registration is "+str(msg),
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    headers = { 
        
    ##'authorization': "Cr79v4zuMHiWcBFm8YK2ElxyqVGR3bALTkIwt1Safp0eQN6XhUkVyhIE9UD1B2opGNCdjHRKgvcWbSm5", 
    'authorization': "9iqLkXfIm3GNWPUd05tolCD71Rb6xsTnegHSEJupcwaAyM4KrvF0jY1rLgcUqG9bnihO7wKDJEMxsZXd", 
    'Content-Type': "application/x-www-form-urlencoded", 
    'Cache-Control': "no-cache"
}
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.text

def generate_otp(mobile):
    if mobile:
        digits = '0123456789'
        new_otp = ''
        for i in range(4):
            new_otp += digits[math.floor(random.random() * 10)]
        return new_otp
    else:
        return False


def generateEmail_otp(mobile):
    if mobile:
        digits = '0123456789'
        new_otp = ''
        for i in range(4):
            new_otp += digits[math.floor(random.random() * 10)]
        return new_otp
    else:
        return False
