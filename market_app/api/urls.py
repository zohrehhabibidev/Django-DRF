from django.urls import path
from .views import market_view, market_single_view, seller_single_view, product_single_view, product_view

urlpatterns = [
    path('market/', market_view),
    path('market/<int:pk>/', market_single_view),
    # path('seller/', sellers_view),
    path('seller/<int:pk>/', seller_single_view, name='seller-single'),

    path('product/', product_view),
    path('product/<int:pk>/', product_single_view),
]
