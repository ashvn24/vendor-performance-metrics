from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, status
# Create your views here.


class VendorAPIView(generics.ListCreateAPIView):
    serializer_class = VendorSerializers
    queryset = Vendor.objects.all()


class ListVendorAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VendorSerializers
    queryset = Vendor.objects.all()
    lookup_field = 'vendor_code'


class PurchaseAPIView(generics.ListCreateAPIView):
    serializer_class = POSerialisers
    queryset = PurchaseOrder.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        vendor_code = self.request.query_params.get('vendor_code')
        if vendor_code:
            data = queryset.filter(vendor=vendor_code)
        return data


class ManagePurchaseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = POSerialisers
    lookup_field = 'po_number'


class VendorPerformanceAPIView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer
    lookup_field = 'vendor_code'

    
class AcknowledgePurchaseAPIView(generics.UpdateAPIView):
    queryset = PurchaseOrder
    serializer_class = POSerialisers
    lookup_field = 'po_number'
    
    def perform_update(self, serializer):
        instance = serializer.save(acknowledgment_date=timezone.now())