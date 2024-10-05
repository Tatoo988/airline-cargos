import unittest
import uuid
from datetime import datetime
from models.address import Address
from models.package import Package
from models.customer import Customer
from models.shipment import Shipment
from enums.shipmentstatus import ShipmentStatus


class TestShipment(unittest.TestCase):

    def setUp(self):
        """Set up a sample shipment for testing."""
        customer = Customer(id=uuid.uuid4(), name="John Doe", address="123 Main St")
        package1 = Package(customer=customer, description="Books", height=10.0, width=5.0, weight=2.0, cost=20.0)
        package2 = Package(customer=customer, description="Clothes", height=12.0, width=6.0, weight=3.0, cost=15.0)
        self.origin = Address(street="123 Main St", city="New York", country="USA", zip="12345")
        self.destination = Address(street="456 Oak St", city="Los Angeles", country="USA", zip="876")
        self.shipment = Shipment(
            origin=self.origin,
            destination=self.destination,
            status=ShipmentStatus.DELIVERED,
            packages=[package1, package2],
            date=datetime.now()
        )

    def test_shipment_attributes(self):
        """Test if shipment attributes are correctly set."""
        self.assertEqual(self.shipment.origin, self.origin)
        self.assertEqual(self.shipment.destination, self.destination)
        self.assertEqual(self.shipment.status, ShipmentStatus.DELIVERED)
        self.assertIsInstance(self.shipment.packages, list)
        self.assertIsInstance(self.shipment.date, datetime)

    def test_shipment_earnings(self):
        """Test if earnings property calculates the total cost of all packages."""
        self.assertEqual(self.shipment.earnings, 35.0)


if __name__ == '__main__':
    unittest.main()
