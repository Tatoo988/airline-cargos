from dataclasses import dataclass, field

from models.customer import Customer


@dataclass
class Package:
    """
    A class representing a package being shipped.

    Attributes:
        customer (Customer): The customer who is sending the package.
        description (str): A brief description of the package contents.
        height (float): The height of the package in units (e.g., centimeters).
        width (float): The width of the package in units (e.g., centimeters).
        weight (float): The weight of the package in units (e.g., kilograms).
        cost (float): The shipping cost for the package. Defaults to 10.
    """

    customer: Customer
    description: str
    height: float
    width: float
    weight: float
    cost: float = field(default=10)