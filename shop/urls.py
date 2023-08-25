from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# /shop/signup/
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.handle_signup, name='handleSignUp'),
    path('login/', views.handle_login, name="handleLogin"),
    path('logout/', views.handle_logout, name="handleLogout"),

    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),

    path('tracker/', views.order, name="TrackingStatus"),
    path('search/', views.search, name="Search"),

    path('checkout/', views.checkout, name="Checkout"),

    path('productView/<int:myid>', views.product_view, name="productView"),

    path('orderView/', views.order_view, name="orderView"),

    path("handlerequest/", views.handle_request, name="HandleRequest")
]