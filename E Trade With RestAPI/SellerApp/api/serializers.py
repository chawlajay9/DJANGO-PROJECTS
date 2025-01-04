from rest_framework import serializers
from SellerApp.models import ModelSeller


class SellerSerializer(serializers.ModelSerializer):
    """
    This class is for outside usage only.
    """
    class Meta:
        model = ModelSeller
        fields = ("companyName",)


class UpdateSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelSeller
        fields = ("companyName", "phone", "website",)




