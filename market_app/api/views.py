from market_app.models import Market, Seller, Product
from .serializers import MarketSerializer, SellerSerializer, ProductSerializer
from rest_framework import generics


class MarketsView(generics.ListCreateAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['fields'] = ['id', 'name']
        return super().get_serializer(*args, **kwargs)


class SellerOfMarketView(generics.ListAPIView):
    serializer_class = SellerSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        market = Market.objects.get(pk=pk)
        return market.sellers.all()


class MarketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class SellerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class ProductsView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
