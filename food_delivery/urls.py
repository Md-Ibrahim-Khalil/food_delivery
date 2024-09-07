from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path("restaurant/", include("restaurant.urls")),
    path("menu/", include("menu.urls")),
    path("category/", include("category.urls")),
    path("item/", include("item.urls")),
]
