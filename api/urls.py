
from django.contrib import admin
from django.urls import path
from . import views
from .views import send_email_api
from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('scrapproduct/', views.getProduct, name="scrap-product"),
    path('scrapproductbycategory/', views.getProductByCategory, name="scrap-product-by-category"),
    path("register/",views.createUser, name="create-user"),
    path("profile/<str:id>",views.getProfile,name="profile"),
    path('updateProfile/',views.update_profile,name="update-profile"),
    path('reviews/', views.get_reviews,name="get-reviews"),
    path('history/<int:id>', views.getHistory,name="get-history"),
    path('send-email/', send_email_api, name='send-email')

    ]



