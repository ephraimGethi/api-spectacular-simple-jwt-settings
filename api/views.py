from django.shortcuts import render

from .seed import DUMMY_PRODUCTS
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_201_CREATED
from .models import Product
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from rest_framework import viewsets
from .schema import product_list_docs,product_viewset_docs
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@product_viewset_docs
class ProductViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

    @product_list_docs
    def list(self,request):
        """
        This method helps to get list of products based on category od the quantity
        """
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")

        if category:
            self.queryset = self.queryset.filter(category__icontains = category)

        if qty:
            self.queryset = self.queryset[:int(qty)]

        serializer = ProductSerializer(self.queryset,many = True)
        return Response(serializer.data)

    
@api_view(['GET'])
def import_dummy_data(request):
    try:
        for entry in DUMMY_PRODUCTS:
            Product.objects.create(
                name = entry["name"],
                description = entry["description"],
                price = entry["price"],
                category = entry["category"],
            )
        response = {"message":"data imported successfully"}
        return Response(response,status=HTTP_201_CREATED)
    except Exception as e:
        error_response = {"message":f"an error occured -  {e}"}
        return Response(error_response,status=HTTP_400_BAD_REQUEST)

@product_list_docs
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def numProducts(request):
    """
    get the total count of the products in our database
    """
    
    data = {
      "count":Product.objects.count()  
    }
    return Response(data)

