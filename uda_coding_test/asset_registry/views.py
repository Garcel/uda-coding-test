from rest_framework import generics

from .models import Asset
from .serializers import AssetSerializer


class AssetListView(generics.ListCreateAPIView):
    """
    Endpoint used to:
        GET the list of registered assets
        POST an asset
    """

    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class AssetListDetailView(generics.RetrieveDestroyAPIView):
    """
    Endpoint used to:
        GET the details of an asset
        DELETE an asset
    """

    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
