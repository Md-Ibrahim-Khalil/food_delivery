from django.urls import path
from .views import (
    OrderCreateView,
    OrderUpdateView,
    OrderListView,
    OrderDeleteView
)


urlpatterns = [
    # localhost:8000/order/create/
    path(
        route="create/",
        view=OrderCreateView.as_view(),
        name="order-create",
    ),
    # localhost:8000/order/update/<int:pk>/
    path(
        route="update/<int:pk>/",
        view=OrderUpdateView.as_view(),
        name="order-create",
    ),
    # localhost:8000/order/list/
    path(
        route="list/",
        view=OrderListView.as_view(),
        name="order-list",
    ),
    # localhost:8000/order/delete/<int:pk>/
    path(
        route="delete/<int:pk>/",
        view=OrderDeleteView.as_view(),
        name="order-delete",
           ),        
]