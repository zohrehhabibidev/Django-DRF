from market_app.models import Market
from .serializers import MarketSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def market_view(request):

    if request.method == 'GET':
        markets = Market.objects.all()
        serializer = MarketSerializer(markets, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MarketSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'DELETE', 'PUT'])
def market_single_view(request, pk):

    if request.method == 'GET':
        try:
            market = Market.objects.get(pk=pk)
            serializer = MarketSerializer(market)
            return Response(serializer.data)

        except Market.DoesNotExist:
            return Response(
                {'message': 'Market not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    if request.method == 'PUT':
        try:
            market = Market.objects.get(pk=pk)

            serializer = MarketSerializer(
                market,
                data=request.data,
                partial=True
            )

            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        except Market.DoesNotExist:
            return Response(
                {'message': 'Market not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    if request.method == 'DELETE':
        try:
            market = Market.objects.get(pk=pk)
            market.delete()

            return Response(
                {'message': 'Market deleted successfully'},
                status=status.HTTP_204_NO_CONTENT
            )

        except Market.DoesNotExist:
            return Response(
                {'message': 'Market not found'},
                status=status.HTTP_404_NOT_FOUND
            )
