from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.


class VendorAPIView(generics.ListCreateAPIView):
    serializer_class = VendorSerializers
    queryset = Vendor.objects.all()
    permission_classes = [IsAuthenticated]


class ListVendorAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VendorSerializers
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    lookup_field = 'vendor_code'


class PurchaseAPIView(generics.ListCreateAPIView):
    serializer_class = POSerialisers
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        vendor_code = self.request.query_params.get('vendor_code')
        if vendor_code:
            queryset = queryset.filter(vendor=vendor_code)
        return queryset


class ManagePurchaseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = POSerialisers
    lookup_field = 'po_number'

    def perform_destroy(self, instance):
        instance.delete()
        return Response({"message": "Purchase order deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class VendorPerformanceAPIView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = VendorPerformanceSerializer
    lookup_field = 'vendor_code'


class AcknowledgePurchaseAPIView(generics.UpdateAPIView):
    queryset = PurchaseOrder
    permission_classes = [IsAuthenticated]
    serializer_class = POSerialisers
    lookup_field = 'po_number'

    def perform_update(self, serializer):
        instance = serializer.save(acknowledgment_date=timezone.now())
