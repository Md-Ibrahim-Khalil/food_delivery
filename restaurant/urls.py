from django.urls import path
from .views import (
    RestaurantCreateView,
    RestaurantUpdateView,
    RestaurantListView,
    RestaurantDeleteView
)


urlpatterns = [
    # localhost:8000/restaurant/create/
    path(
        route="create/",
        view=RestaurantCreateView.as_view(),
        name="restaurant-create",
    ),
    # localhost:8000/restaurant/update/<int:pk>/
    path(
        route="update/<int:pk>/",
        view=RestaurantUpdateView.as_view(),
        name="restaurant-create",
    ),
    # localhost:8000/restaurant/list/
    path(
        route="list/",
        view=RestaurantListView.as_view(),
        name="restaurant-list",
    ),
    # localhost:8000/restaurant/delete/<int:pk>/
    path(
        route="delete/<int:pk>/",
        view=RestaurantDeleteView.as_view(),
        name="restaurant-delete",
    ),        
]