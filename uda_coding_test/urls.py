from django.urls import include, re_path

urlpatterns = [
    re_path(r'^', include('uda_coding_test.asset_registry.urls')),
]
