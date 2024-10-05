import unittest
import uuid
from datetime import datetime
from models.shipment import Shipment
from models.address import Address
from models.package import Package
from models.customer import Customer
from enums.shipmentstatus import ShipmentStatus
from models.airline import AirLine


class TestAirLine(unittest.TestCase):

    def setUp(self):
        """Set up sample shipments and an airline for testing."""
        customer = Customer(id=uuid.uuid4(), name="John Doe", address="123 Main St")
        customer2 = Customer(id=uuid.uuid4(), name="William Smith", address="456 Fake St")
        package1 = Package(customer=customer, description="Books", height=10.0, width=5.0,
                           weight=2.0)
        package2 = Package(customer=customer, description="Clothes", height=12.0, width=6.0,
                           weight=3.0)
        package3 = Package(customer=customer2, description="Food", height=6.0, width=5.0,
                           weight=4.0)

        self.origin = Address(street="123 Main St", city="New York", country="USA", zip="2000")
        self.destination = Address(street="456 Oak St", city="Los Angeles", country="USA",
                                   zip="2000")

        self.shipment1 = Shipment(
            origin=self.origin,
            destination=self.destination,
            status=ShipmentStatus.DELIVERED,
            packages=[package1, package3],
            date=datetime(2023, 10, 5)
        )

        self.shipment2 = Shipment(
            origin=self.origin,
            destination=self.destination,
            status=ShipmentStatus.IN_TRANSIT,
            packages=[package2],
            date=datetime(2023, 10, 5)
        )

        self.airline = AirLine(name="FastAir", shipments=[self.shipment1, self.shipment2])

    def test_airline_attributes(self):
        """Test if airline attributes are correctly set."""
        self.assertEqual(self.airline.name, "FastAir")
        self.assertIsInstance(self.airline.shipments, list)

    def test_airline_earnings(self):
        """Test if earnings for a specific date consider only delivered shipments."""
        report = self.airline.report(datetime(2023, 10, 5).date())
        self.assertEqual(report[0], 2)  # Only the delivered shipment counts
        self.assertEqual(report[1], 20.0)  # Only the delivered shipment counts


if __name__ == '__main__':
    unittest.main()
