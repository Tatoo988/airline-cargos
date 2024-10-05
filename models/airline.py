from dataclasses import dataclass
from datetime import date
from typing import List

from enums.shipmentstatus import ShipmentStatus
from models.shipment import Shipment


@dataclass
class AirLine:
    """
    A class representing an airline and its associated shipments.

    Attributes:
        name (str): The name of the airline.
        shipments (List[Shipment]): A list of Shipment objects associated with the airline.
    """

    name: str
    shipments: List[Shipment]

    def report(self, shipment_date: date) -> tuple[int, float]:
        """
            Generates a report of the total number of packages and earnings from shipments delivered on a specific date.

            Args:
                shipment_date (date): The date for which to generate the report of delivered shipments.

            Returns:
                tuple[int, float]: A tuple containing the total number of packages delivered and the total earnings
                                   for shipments delivered on the specified date.

            The function filters shipments based on the given date and delivery status, then calculates the sum of
            packages and earnings for all shipments delivered on that date. It prints the result and returns the totals.
            """
        report_list= ((shipment.packages_count, shipment.earnings) for shipment in self.shipments if
                    shipment.date.date() == shipment_date and
                    shipment.status == ShipmentStatus.DELIVERED)
        packages_count, earnings = map(sum, zip(*report_list))
        print(f'total earnings for shipments delivered on {shipment_date}: {packages_count} packages, earnings: ${earnings}' )
        return packages_count, earnings

