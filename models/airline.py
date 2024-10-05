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

    def earnings(self, shipment_date: date) -> float:
        """
        Calculate the total earnings for shipments delivered on a specific date.

        Args:
            shipment_date (date): The date to filter shipments by.

        Returns:
            float: The total earnings from shipments that were delivered on the
            given shipment_date. Only shipments with a status of 'DELIVERED' are
            considered.
        """
        return sum((shipment.earnings for shipment in self.shipments if
                    shipment.date.date() == shipment_date and
                    shipment.status == ShipmentStatus.DELIVERED))
