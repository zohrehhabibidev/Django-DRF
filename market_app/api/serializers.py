from rest_framework import serializers
from market_app.models import Market, Seller, Product


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)

            for field_name in existing - allowed:
                self.fields.pop(field_name)


class MarketSerializer(DynamicFieldsModelSerializer):

    sellers = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='seller-single'
    )

    class Meta:
        model = Market
        fields = '__all__'


class SellerSerializer(DynamicFieldsModelSerializer):
    markets = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        many=True
    )

    class Meta:
        model = Seller
        fields = '__all__'


class ProductSerializer(DynamicFieldsModelSerializer):
    market = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all()
    )
    seller = serializers.PrimaryKeyRelatedField(
        queryset=Seller.objects.all()
    )

    class Meta:
        model = Product
        fields = '__all__'
