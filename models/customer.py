import uuid
from dataclasses import dataclass


@dataclass
class Customer:
    """
    A class representing a customer.

    Attributes:
        id (uuid.UUID): A unique identifier for the customer.
        name (str): The name of the customer.
        address (str): The address of the customer.
    """

    id: uuid.UUID
    name: str
    address: str

    def __repr__(self) -> str:
        """
        Return a string representation of the Customer instance.

        Returns:
            str: The name of the customer.
        """
        return self.name
