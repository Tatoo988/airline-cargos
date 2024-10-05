from datetime import datetime


def shipments_report_per_day(date: datetime.date):
    return sum((shipment.earnings for shipment in shipments if shipment.date.date==date))
