from django.urls import path
from .views import market_view, market_single_view

urlpatterns = [
    path('', market_view),
    path('<int:pk>/', market_single_view),
]
