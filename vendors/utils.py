from .models import PurchaseOrder
from django.db.models import F, Avg, ExpressionWrapper, DurationField, FloatField
from django.db.models.functions import Extract, Cast


def calculate_on_time_delivery_rate(vendor):
    total_orders = PurchaseOrder.objects.filter(
        vendor=vendor, status='completed').count()
    on_time_orders = PurchaseOrder.objects.filter(
        status='completed', delivery_date__lte=F('expected_delivery_date')
    ).count()
    
    print(on_time_orders, total_orders)
    if total_orders > 0:
        return on_time_orders / total_orders
    return 0.0


def calculate_quality_rating_avg(vendor):
    quality_rating_avg = PurchaseOrder.objects.filter(
        vendor=vendor,
        status='completed',
        quality_rating__isnull=False).aggregate(
        quality_rating_avg=Avg('quality_rating'))['quality_rating_avg']

    return quality_rating_avg or 0.0


def calculate_average_response_time(vendor):
    avg_response_time_seconds = PurchaseOrder.objects.filter(
        vendor=vendor,
        acknowledgment_date__isnull=False
    ).annotate(
        response_time=ExpressionWrapper(
            F('acknowledgment_date') - F('issue_date'),
            output_field=DurationField()  # Use DurationField
        )
    ).aggregate(
        avg_response_time_seconds=Avg(
            Cast(Extract('response_time', 'seconds'), output_field=FloatField()))
    )['avg_response_time_seconds']

    if avg_response_time_seconds:
        return avg_response_time_seconds
    return 0.0


def calculate_fulfillment_rate(vendor):
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    fulfilled_orders = PurchaseOrder.objects.filter(
        vendor=vendor, status='completed').count()

    if total_orders > 0:
        return fulfilled_orders / total_orders
    return 0.0
