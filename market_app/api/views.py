from market_app.models import Market, Seller, Product
from .serializers import MarketSerializer, SellerSerializer, ProductDetailSerializer, ProductCreateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def market_view(request):

    if request.method == 'GET':
        markets = Market.objects.all()
        serializer = MarketSerializer(
            markets,
            many=True,
            context={'request': request})
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


# @api_view(['GET', 'POST'])
# def sellers_view(request):
#     if request.method == 'GET':
#         sellers = Seller.objects.all()
#         serializer = SellerDetailSerializer(sellers, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = SellerCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


@api_view(['GET', 'DELETE', 'PUT'])
def seller_single_view(request, pk):

    if request.method == 'GET':
        try:
            seller = Seller.objects.get(pk=pk)
            serializer = SellerSerializer(seller)
            return Response(serializer.data)

        except Seller.DoesNotExist:
            return Response(
                {'message': 'Seller  not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    if request.method == 'PUT':
        try:
            seller = Seller.objects.get(pk=pk)

            serializer = SellerSerializer(
                seller,
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

        except Seller.DoesNotExist:
            return Response(
                {'message': 'Seller  not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    if request.method == 'DELETE':
        try:
            seller = Seller.objects.get(pk=pk)
            seller.delete()

            return Response(
                {'message': 'Seller  deleted successfully'},
                status=status.HTTP_204_NO_CONTENT
            )

        except Seller.DoesNotExist:
            return Response(
                {'message': 'Seller  not found'},
                status=status.HTTP_404_NOT_FOUND
            )


@api_view(['GET', 'POST'])
def product_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductCreateSerializer(data=request.data)

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
def product_single_view(request, pk):
    if request.method == 'GET':
        try:
            pruduct = Product.objects.get(pk=pk)
            serializer = ProductDetailSerializer(pruduct)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(
                {'message': 'Product not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    if request.method == 'PUT':
        try:
            pruduct = Product.objects.get(pk=pk)

            serializer = ProductCreateSerializer(
                pruduct,
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

        except Product.DoesNotExist:
            return Response(
                {'message': 'Pruduct not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    if request.method == 'DELETE':
        try:
            product = Product.objects.get(pk=pk)
            product.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Product.DoesNotExist:
            return Response(
                {'message': 'Product not found'},
                status=status.HTTP_404_NOT_FOUND
            )
