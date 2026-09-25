from rest_framework import serializers
from market_app.models import Market, Seller, Product


def validate_no_x(value):
    errors = []
    if 'X' in value:
        errors. append('no X in Filed')
        if 'Y' in value:
            errors.append('no Y in Field')
    if errors:
        raise serializers.ValidationError(errors)
    return value


class MarketSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=255)
    # location = serializers.CharField(
    #     max_length=255, validators=[validate_no_x])
    # description = serializers.CharField(max_length=255)
    # net_worth = serializers.DecimalField(max_digits=100, decimal_places=2)
    sellers = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='seller-single'
    )

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)

            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Market
        fields = '__all__'

    def create(self, validated_data):
        return Market.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.net_worth = validated_data.get(
            'net_worth', instance.net_worth)
        instance.save()
        return instance


# class MarketHyperSerializer(MarketSerializer):
#     sellers = None

#     class Meta:
#         model = Market
#         fields = '__all__'

# class SellerDetailSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#     contact_info = serializers.CharField()
#     markets = MarketSerializer(many=True, read_only=True)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.contact_info = validated_data.get(
#             'contact_info', instance.contact_info)
#         instance.save()
#         return instance


# class SellerCreateSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     contact_info = serializers.CharField()
#     markets = serializers.ListField(
#         child=serializers.IntegerField(), write_only=True)

#     def validate_markets(self, value):
#         markets = Market.objects.filter(id__in=value)

#         if len(markets) != len(value):
#             raise serializers.ValidationError(
#                 'One or more market IDs not found')
#         return value

#     def create(self, validated_data):
#         market_ids = validated_data.pop('markets')
#         seller = Seller.objects.create(**validated_data)
#         markets = Market.objects.filter(id__in=market_ids)
#         seller.markets.set(markets)
#         return seller

class SellerSerializer(serializers.ModelSerializer):
    markets = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        many=True
    )

    class Meta:
        model = Seller
        fields = '__all__'


class ProductDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=50, decimal_places=2)
    market = serializers.StringRelatedField(read_only=True)
    seller = serializers.StringRelatedField(
        read_only=True)


class ProductCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=50, decimal_places=2)
    market = serializers.IntegerField()
    seller = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(
            name=validated_data["name"],
            description=validated_data["description"],
            price=validated_data["price"],
            market=Market.objects.get(pk=validated_data["market"]),
            seller=Seller.objects.get(pk=validated_data["seller"])
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.price = validated_data.get('price', instance.price)

        if 'market' in validated_data:
            instance.market = Market.objects.get(
                pk=validated_data["market"]
            )
        if 'seller' in validated_data:
            instance.seller = Seller.objects.get(
                pk=validated_data["seller"]
            )

        instance.save()
        return instance
