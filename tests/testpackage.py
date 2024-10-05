import unittest
import uuid

from models.customer import Customer
from models.package import Package


class TestPackage(unittest.TestCase):

    def setUp(self):
        """Set up a sample package for testing."""
        customer = Customer(id=uuid.uuid4(), name="John Doe", address="123 Main St")
        self.package = Package(customer=customer, description="Books", height=10.0, width=5.0, weight=2.0)

    def test_package_attributes(self):
        """Test if package attributes are correctly set."""
        self.assertIsInstance(self.package.customer, Customer)
        self.assertEqual(self.package.description, "Books")
        self.assertEqual(self.package.height, 10.0)
        self.assertEqual(self.package.width, 5.0)
        self.assertEqual(self.package.weight, 2.0)
        self.assertEqual(self.package.cost, 10.0)  # Default cost

    def test_package_custom_cost(self):
        """Test package cost when provided explicitly."""
        customer = Customer(id=uuid.uuid4(), name="Jane Doe", address="456 Oak St")
        package_with_cost = Package(customer=customer, description="Clothes", height=15.0, width=10.0, weight=3.0, cost=20.0)
        self.assertEqual(package_with_cost.cost, 20.0)


if __name__ == '__main__':
    unittest.main()
