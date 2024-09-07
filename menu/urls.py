from django.urls import path
from .views import (
    MenuCreateView,
    MenuUpdateView,
    MenuListView,
    MenuDeleteView
)


urlpatterns = [
    # localhost:8000/menu/create/
    path(
        route="create/",
        view=MenuCreateView.as_view(),
        name="menu-create",
    ),
    # localhost:8000/menu/update/<int:pk>/
    path(
        route="update/<int:pk>/",
        view=MenuUpdateView.as_view(),
        name="menu-create",
    ),
    # localhost:8000/menu/list/
    path(
        route="list/",
        view=MenuListView.as_view(),
        name="menu-list",
    ),
    # localhost:8000/menu/delete/<int:pk>/
    path(
        route="delete/<int:pk>/",
        view=MenuDeleteView.as_view(),
        name="menu-delete",
    ),        
]