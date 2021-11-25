
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from petapp import views
from rest_framework import serializers, viewsets

# Routers provide an easy way of automatically determining the URL conf.

# urlpatterns = [

#     path('productlist/', views.all_products),
#     path('products/<int:pk>',views.product_detail),
  
   
# ]
# if settings.DEBUG:
#     urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





from django.conf.urls import url,include
# from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views as restview
from petapp.views import  CustomerRegistrationView,ProductView,CustomerLoginView,CustomerProfileView
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.dashboard,name='HOME'),
    #######################################################################################################################
                                                        ## Customer APIs ##
    #######################################################################################################################
    #### Register
    url(r'^customer-Registration/$',CustomerRegistrationView.as_view(), name='customer-Registration'),
#### Profile
    url(r'^get-cutomerProfile/$',CustomerProfileView.as_view(),name='get-customerProfile'),
 #### Login

    url(r'^customer-Login/$',CustomerLoginView.as_view(), name='customer-Login'),
  #### Product
    path('productlist/', ProductView.as_view(), name='all_products'),
    path('products/<int:pk>',ProductView.as_view(), name='product_detail'),
  
   

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

