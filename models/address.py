from dataclasses import dataclass


@dataclass
class Address:
    street: str
    city: str
    zip: str
    country: str