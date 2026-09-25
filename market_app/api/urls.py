from django.urls import path
from .views import (
    MarketsView,
    MarketDetailView,
    SellerDetailView,
    SellerOfMarketView,
    ProductsView,
    ProductDetailView,
)

urlpatterns = [
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketDetailView.as_view(), name='market-detail'),
    path('market/<int:pk>/sellers/', SellerOfMarketView.as_view()),

    path('seller/<int:pk>/', SellerDetailView.as_view(), name='seller-single'),

    path('product/', ProductsView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
]
