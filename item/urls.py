from django.urls import path
from .views import (
    ItemCreateView,
    ItemUpdateView,
    ItemListView,
    ItemDeleteView
)


urlpatterns = [
    # localhost:8000/item/create/
    path(
        route="create/",
        view=ItemCreateView.as_view(),
        name="item-create",
    ),
    # localhost:8000/item/update/<int:pk>/
    path(
        route="update/<int:pk>/",
        view=ItemUpdateView.as_view(),
        name="item-create",
    ),
    # localhost:8000/item/list/
    path(
        route="list/",
        view=ItemListView.as_view(),
        name="item-list",
    ),
    # localhost:8000/item/delete/<int:pk>/
    path(
        route="delete/<int:pk>/",
        view=ItemDeleteView.as_view(),
        name="item-delete",
    ),        
]