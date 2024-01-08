from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('collections/',views.collections, name='collections'),
    path('collections/<str:name>', views.collectionsView, name='collections'),
    path('collections/<str:cname>/<str:pname>', views.product_info, name='product_info'),
    path('addtocart',views.add_to_cart, name='addtocart'),
    path('cart',views.cart_page,name='cart'),
    path('remove_cart/<str:cid>',views.remove_cart,name='remove_cart')
    
   
]   
