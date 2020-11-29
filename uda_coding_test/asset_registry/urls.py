from django.urls import path
from .views import AssetListView, AssetListDetailView

urlpatterns = [
    path("assets/", AssetListView.as_view(), name="assets_list"),
    path("assets/<int:pk>/", AssetListDetailView.as_view(), name="assets_detail"),
]
