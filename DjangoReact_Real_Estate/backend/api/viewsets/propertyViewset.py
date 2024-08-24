from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from api.models import Property
from api.serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['address', 'price', 'bedrooms', 'bathrooms']
    ordering_fields = ['price', 'bedrooms', 'bathrooms']

    def get_queryset(self):
        # Check if a query parameter 'myproperties' is provided
        myproperties = self.request.query_params.get('myproperties', None)

        if myproperties == 'true':
            # Fetch properties owned by the current user
            return Property.objects.filter(owner=self.request.user)
        elif myproperties == 'false':
            # Fetch properties where the current user is NOT the owner
            return Property.objects.exclude(owner=self.request.user)
        
        # Otherwise, return all properties
        return Property.objects.all()

    def perform_create(self, serializer):
        # Automatically set the current user as the owner of the property
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        # Ensure only the owner can update the property
        instance = self.get_object()
        if instance.owner != self.request.user:
            return Response({"error": "You are not authorized to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        serializer.save()

    def perform_destroy(self, instance):
        # Ensure only the owner can delete the property
        if instance.owner != self.request.user:
            return Response({"error": "You are not authorized to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        instance.delete()
