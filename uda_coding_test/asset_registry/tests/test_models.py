from django.test import TestCase

from ..models import Asset, GeoPosition


class GeoPositionModelTests(TestCase):

    def setUp(self):
        self.geom = GeoPosition.objects.create(
            latitude=42.5507956317338,
            longitude=-6.603349658436887,
        )

    def test_str_return_the_expected_result(self):
        """
        str() returns the asset.geom
        """
        self.assertEqual(str(self.geom), '42.5507956317338, -6.603349658436887')


class AssetModelTests(TestCase):

    def setUp(self):
        self.asset = Asset.objects.create(
            geom=GeoPosition.objects.create(
                latitude=42.5507956317338,
                longitude=-6.603349658436887,
            ),
            area=1,
        )

    def test_str_return_the_expected_result(self):
        """
        str() returns the asset.geom
        """
        self.assertEqual(str(self.asset), '42.5507956317338, -6.603349658436887')

