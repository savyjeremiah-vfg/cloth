from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.home, name='home'),
  path('categories/', views.home, name='categories'),
  path('products/', views.home, name='products'),
  path("shop/",views.shop ,name="shop"),
  path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
  path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
  path('cart/', views.cart, name='cart'),
  path('checkout/', views.checkout, name='checkout'),
  path('contact/', views.contact, name='contact'),
]