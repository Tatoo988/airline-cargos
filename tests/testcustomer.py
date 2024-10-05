import unittest
import uuid
from models.customer import Customer


class TestCustomer(unittest.TestCase):

    def setUp(self):
        """Set up a sample customer for testing."""
        self.customer = Customer(id=uuid.uuid4(), name="John Doe", address="123 Main St")

    def test_customer_attributes(self):
        """Test if customer attributes are correctly set."""
        self.assertIsInstance(self.customer.id, uuid.UUID)
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.address, "123 Main St")

    def test_customer_repr(self):
        """Test the __repr__ method returns the customer's name."""
        self.assertEqual(repr(self.customer), "John Doe")


if __name__ == '__main__':
    unittest.main()