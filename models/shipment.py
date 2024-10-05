from dataclasses import dataclass
from datetime import datetime
from typing import List

from enums.shipmentstatus import ShipmentStatus
from models.address import Address
from models.package import Package


@dataclass
class Shipment:
    """
    A class representing a shipment consisting of multiple packages.

    Attributes:
        origin (Address): The address from where the shipment originates.
        destination (Address): The address to which the shipment is headed.
        status (ShipmentStatus): The current status of the shipment (e.g., DELIVERED, IN_TRANSIT).
        packages (List[Package]): A list of Package objects included in the shipment.
        date (datetime): The date and time when the shipment was created or processed.
    """

    origin: Address
    destination: Address
    status: ShipmentStatus
    packages: List[Package]
    date: datetime

    @property
    def earnings(self) -> float:
        """
        Calculate the total earnings from the shipment based on the cost of the packages.

        Returns:
            float: The sum of the costs of all packages in the shipment.
        """
        return sum((package.cost for package in self.packages))

    @property
    def packages_count(self):
        return len(self.packages)