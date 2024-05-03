from django.urls import path
from .views import *

urlpatterns = [
    path('vendors/', VendorAPIView.as_view()),
    path('vendors/<int:vendor_code>/', ListVendorAPIView.as_view()),
    path('vendors/<int:vendor_code>/performance/', VendorPerformanceAPIView.as_view()),
    
    path('purchase_orders/', PurchaseAPIView.as_view()),
    path('purchase_orders/<str:po_number>/', ManagePurchaseAPIView.as_view()),
    path('purchase_orders/<str:po_number>/acknowledge/', AcknowledgePurchaseAPIView.as_view()),
]   
