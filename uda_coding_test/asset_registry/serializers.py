from rest_framework import serializers

from .models import Asset, GeoPosition


class GeoPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeoPosition
        fields = ['latitude', 'longitude']


class AssetSerializer(serializers.ModelSerializer):
    geom = GeoPositionSerializer(required=True)

    class Meta:
        model = Asset
        fields = '__all__'

    def create(self, validated_data):
        """
        Needed as DRF doesn't natively support `create` method for nested serializers.
        https://www.django-rest-framework.org/api-guide/serializers/#writing-create-methods-for-nested-representations
        """
        geom_data = validated_data.pop('geom')
        geom = GeoPosition.objects.create(**geom_data)
        asset = Asset.objects.create(geom=geom, **validated_data)

        return asset
