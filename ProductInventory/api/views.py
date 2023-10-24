from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer, ProductUpdateSerializer


class NewProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AvailableProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(status=True)
    serializer_class = ProductSerializer


class UnavailableProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(status=False)
    serializer_class = ProductSerializer


class ProductStatusUpdateView(APIView):
    def patch(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        new_status = request.data.get('status', None)
        new_quantity = request.data.get('quantity', None)
        if new_status is not None and new_quantity is not None:
            if new_status not in ['available', 'unavailable']:
                return Response({'error': "Status value is invalid"}, status=status.HTTP_400_BAD_REQUEST)
            if int(new_quantity) < 0:
                return Response({'error': "Quantity value is invalid"}, status=status.HTTP_400_BAD_REQUEST)
            if new_status == 'available' and new_quantity == 0:
                return Response({'error': "Status can not be available when quantity is 0."}, status=status.HTTP_400_BAD_REQUEST)
            if new_status == 'unavailable' and new_quantity != 0:
                raise Response({'error': "Status can not be unavailable when quantity is more than 0."}, status=status.HTTP_400_BAD_REQUEST)
        
            new_status = True if "available" else False
            serializer = ProductUpdateSerializer(product, data={"status": new_status, "quantity": new_quantity}, partial=True)

            if serializer.is_valid():
                serializer.save()

                # Handle status_enum property when returning the response
                data = serializer.data
                data['status'] = product.status_enum
                return Response(data, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': "Please provide required field's [status, quantity] values in your request."}, status=status.HTTP_400_BAD_REQUEST)