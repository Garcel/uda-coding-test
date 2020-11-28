from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from uda_coding_test.asset_registry import views
from uda_coding_test.asset_registry.models import Asset, GeoPosition


class AssetListViewTest(APITestCase):
    # number of assets for asset list view
    number_of_assets = 3

    @classmethod
    def setUpTestData(cls):
        # dummy assets here...
        for asset_id in range(cls.number_of_assets):
            Asset.objects.create(
                geom=GeoPosition.objects.create(
                    latitude=asset_id,
                    longitude=asset_id,
                ),
                area=asset_id,
            )

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.AssetListView.as_view()
        self.uri = '/assets/'

    def test_view_url_exists_at_desired_location(self):
        request = self.factory.get(self.uri)
        response = self.view(request)

        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_assets_list(self):
        """
        Ensure that all the registered assets are returned.
        """
        request = self.factory.get(self.uri)
        response = self.view(request)

        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

        # Assert response content
        self.assertEqual(len(response.data), self.number_of_assets)

        # Assert each asset content
        for asset_pos in range(self.number_of_assets):
            asset_data = response.data[asset_pos]
            # Mandatory
            self.assertAlmostEqual(float(asset_data['geom']['latitude']), asset_pos)
            self.assertAlmostEqual(float(asset_data['geom']['longitude']), asset_pos)
            self.assertEqual(asset_data['area'], asset_pos)

            # Optional
            self.assertIsNone(asset_data['address'])
            self.assertIsNone(asset_data['garage'])
            self.assertIsNone(asset_data['rooms'])
            self.assertIsNone(asset_data['other'])

    def test_create_asset_without_geom_fails(self):
        """
        Ensure that the asset creation fails when the `geom` property is not provided.
        """
        data = {
            'area': 1
        }

        request = self.factory.post(self.uri, data, format='json')
        response = self.view(request)

        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_asset_without_area_fails(self):
        """
        Ensure that the asset creation fails when the `area` property is not provided.
        """
        data = {
            'geom': {
                'latitude': 42.5507956317338,
                'longitude': -6.603349658436887
            }
        }

        request = self.factory.post(self.uri, data, format='json')
        response = self.view(request)

        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_asset_with_mandatory_props_is_successful(self):
        """
        Ensure that the new asset is created properly when only the asset's mandatory properties are provided.
        """
        data = {
            'geom': {
                'latitude': 42.5507956317338,
                'longitude': -6.603349658436887
            },
            'area': 1
        }

        request = self.factory.post(self.uri, data, format='json')
        response = self.view(request)

        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert response content
        # Mandatory
        self.assertAlmostEqual(float(response.data['geom']['latitude']), data['geom']['latitude'])
        self.assertAlmostEqual(float(response.data['geom']['longitude']), data['geom']['longitude'])
        self.assertEqual(response.data['area'], data['area'])

        # Optional
        self.assertIsNone(response.data['address'])
        self.assertIsNone(response.data['garage'])
        self.assertIsNone(response.data['rooms'])
        self.assertIsNone(response.data['other'])

    def test_create_asset_with_all_props_is_successful(self):
        """
        Ensure that the new asset is created properly when all the asset's properties are provided.
        """
        data = {
            'geom': {
                'latitude': 42.5507956317338,
                'longitude': -6.603349658436887
            },
            'area': 1,
            'address': 'foo street',
            'garage': True,
            'other': {
                'elevator': 'True'
            },
            'rooms': 3
        }

        request = self.factory.post(self.uri, data, format='json')
        response = self.view(request)

        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert response content
        # Mandatory
        self.assertAlmostEqual(float(response.data['geom']['latitude']), data['geom']['latitude'])
        self.assertAlmostEqual(float(response.data['geom']['longitude']), data['geom']['longitude'])
        self.assertEqual(response.data['area'], data['area'])

        # Optional
        self.assertEqual(response.data['address'], data['address'])
        self.assertEqual(response.data['garage'], data['garage'])
        self.assertEqual(response.data['other']['elevator'], data['other']['elevator'])
        self.assertEqual(response.data['rooms'], data['rooms'])
