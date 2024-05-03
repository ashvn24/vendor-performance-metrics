from celery import shared_task
from .models import HistoricalPerformance, Vendor


@shared_task(bind=True)
def create_historical_performance(self, vendor):
    print(vendor)
    vendor = Vendor.objects.get(pk=vendor)
    history = HistoricalPerformance.objects.create(
        vendor=vendor,
        on_time_delivery_rate=vendor.on_time_delivery_rate,
        quality_rating_avg=vendor.quality_rating_avg,
        average_response_time=vendor.average_response_time,
        fulfillment_rate=vendor.fulfillment_rate,
    )
    history.save()
