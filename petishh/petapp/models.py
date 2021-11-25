from os import defpath, name
from django.db import models

# Create your models here.
from django.db import models
# from user_profile.models import User
from django.contrib.auth.models import User
from django.db.models.fields import CharField, SlugField
from django.db.models.fields.files import ImageField
from django.conf import settings
# from django.http.request import UploadHandlerList


#######################################################################################################################
                                                        ## Category, Product Models ##
#######################################################################################################################

class Category(models.Model):
    name=models.CharField(max_length=255, db_index=True)
    slug= models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural='categories'

    def __str__(self):
        return self.name   



class Product(models.Model):
    category= models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255, default='admin')
    description=models.TextField(blank=True)
    image= models.ImageField(upload_to='images/')
    slug= models.SlugField(max_length=255)
    price=  models.DecimalField(max_digits=5, decimal_places=2)
    in_stock= models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural='Products'
        ordering=('-created',)
    def __str__(self):
        return self.title

# class Cart(models.Model):
#     name=models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product' )
#     price=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_add')
#     wish_list=models.BooleanField(default=False)
#     updated=models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name_plural='Carts'
#         ordering=('-price',)
#     def __str__(self):
#         return self.price   


 #######################################################################################################################
                                                        ## Auth Users Models ##
    #######################################################################################################################


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import datetime
from django.utils import timezone

class Users(AbstractUser):
    # username = models.CharField(max_length = 50, blank = True, null = True, unique = False) 
    referelcode = models.CharField(max_length=20, default="", blank=True)
    refererid = models.CharField(max_length=20, default="", blank=True,null=True)
    wallet = models.IntegerField(default=0)
    dateofbirth = models.CharField(max_length=20, default="", blank=True)
    adhaarcard = models.CharField(max_length=20, default="", blank=True)

    phone_no = models.CharField(max_length=20, default="", blank=True)
    secondary_no = models.CharField(max_length=20, default="", blank=True)
    is_phone_verified = models.BooleanField(default=False, verbose_name='Phone Verification')
    is_email_verified = models.BooleanField(default=True, verbose_name='Email Verification')
    verified_code = models.CharField(max_length=30)
    reset_password = models.BooleanField(default=False)
    address = models.CharField(max_length=255, default="", blank=True, null=True)
    home_address = models.CharField(max_length=255, default="", blank=True, null=True)
    profile_image = models.CharField(max_length=225, blank=True, null=True)
    
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    modified_date = models.DateTimeField(default=datetime.now, blank=True)
    is_blocked = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    owner_name = models.CharField(max_length=255, blank=True, null=True)
    shop_name = models.CharField(max_length=255, blank=True, null=True)
    
    registration_date = models.DateTimeField(null=True, blank=True)
    gst_state = models.CharField(max_length=255, blank=True, null=True)
    gst_type = models.CharField(max_length=255, blank=True, null=True)
   
    shop_city = models.CharField(max_length=255, blank=True, null=True)
    shop_landmark = models.CharField(max_length=255, null=True)
    pin_code = models.IntegerField(default=0, null=True)
    shop_image = models.CharField(max_length=225, blank=True, null=True)
   
    user_type = models.IntegerField(default=0, null=True)
    account  = models.CharField(max_length=225, blank=True, null=True)
    is_shop_verified = models.BooleanField(default=False)
    
    owner_image = models.CharField(max_length=225, blank=True, null=True)
    floor_no = models.IntegerField(default=0, null=True)
    mall_name = models.CharField(max_length=225, blank=True, null=True)
    state = models.CharField(max_length=225, blank=True, null=True)
    shop_area = models.CharField(max_length=225, blank=True, null=True)
    shop_comment = models.CharField(max_length=225, blank=True, null=True)
    owner_comment = models.CharField(max_length=225, blank=True, null=True)
    is_submitted =models.BooleanField(default=False)
    is_auth =models.BooleanField(default=False)
    status =models.BooleanField(default=False)
    comment = models.CharField(max_length=500, blank=True, null=True)    

    
    class Meta:
        db_table = 'auth_user'

    def get_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.username

# from django.contrib.auth.models import User

# class Profile(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE)
#     image=models.ImageField()

#     def __str__(self):
#         return f'{self.user.username}Profile'


class Profileinfo(models.Model):
    user 			    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_profile_info',null=True)
    Information         = models.TextField(blank=True, null=True)
    philisophy          = models.TextField(blank=True, null=True)
    achievements        = models.TextField(blank=True, null=True)
    toprecipe           = models.TextField(blank=True, null=True)
    

    is_approved = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)



class EmailCodeVerification(models.Model):
	user 			    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_verification')
	email 			    = models.CharField(max_length=255, blank=True, null=True)
	verification_code   = models.CharField(max_length=20, blank=True, null=True)
	is_varified 		= models.BooleanField(default=False)
	is_deleted 			= models.BooleanField(default=False)
	created_date 		= models.DateTimeField(default=datetime.now, blank=True)
	modified_date 		= models.DateTimeField(default=datetime.now, blank=True)