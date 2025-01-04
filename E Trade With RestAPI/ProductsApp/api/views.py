from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    DestroyAPIView, RetrieveUpdateAPIView
)
from ProductsApp.models import ModelProduct, ModelProductCategory
from .serializers import ProductsSerializer, CreateUpdateProductSerializer, CreateUpdateCategorySerializer
from SellerApp.models import ModelSeller
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


class AllProductListView(ListAPIView):
    # Lists all products randomly
    serializer_class = ProductsSerializer

    def get_queryset(self):
        # Retrieve products that are not drafts, ordered randomly
        return ModelProduct.objects.filter(draft=True).order_by("?")

class ListProductByCategory(ListAPIView):
    # Lists products by category
    serializer_class = ProductsSerializer
    lookup_field     = "slug"

    def get_queryset(self):
        # Retrieve products based on category slug that are not drafts
        return ModelProduct.objects.filter(draft=True, category__slug=self.kwargs.get("slug"))

class DetailProductView(RetrieveAPIView):
    # Retrieves one product by its slug
    queryset         = ModelProduct.objects.all()
    lookup_field     = "slug"
    serializer_class = ProductsSerializer


class CreateProductView(CreateAPIView):
    queryset         = ModelProduct.objects.all()
    serializer_class = CreateUpdateProductSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create a product

    def perform_create(self, serializer):
        # Check if the authenticated user is associated with a seller
        seller = ModelSeller.objects.filter(user=self.request.user)
        if not seller:
            # Return an error message if no seller is found
            return JsonResponse({"message": "You need to create a seller account to sell products."}, status=403)
        else:
            # Save the product with the associated seller
            serializer.save(seller=seller[0])


class DeleteProductView(DestroyAPIView):
    queryset         = ModelProduct.objects.all()
    serializer_class = ProductsSerializer
    lookup_field     = "slug"  # Delete a product based on its slug


class UpdateProductView(RetrieveUpdateAPIView):
    queryset         = ModelProduct.objects.all()
    serializer_class = CreateUpdateProductSerializer
    lookup_field     = "slug"  # Update a product based on its slug


class CreateCategoryView(CreateAPIView):
    queryset         = ModelProductCategory.objects.all()
    serializer_class = CreateUpdateCategorySerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create a product
