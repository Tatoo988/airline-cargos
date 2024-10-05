# Shipment and Package Management System

This project provides a simple system for managing shipments, packages, customers, and airline earnings. It includes models representing customers, packages, shipments, and airlines, and supports calculating earnings based on delivered packages.

## Features

- **Customer Management**: Represents customers with a unique identifier, name, and address.
- **Package Management**: Allows tracking of packages with details like height, width, weight, and cost.
- **Shipment Tracking**: Shipments have origins, destinations, status (e.g., delivered or in transit), and packages.
- **Airline Earnings Calculation**: An airline can have multiple shipments, and it calculates its earnings based on delivered shipments.

## Project Structure

```plaintext
.
├── enums
│   └── shipmentstatus.py    # Enum for shipment statuses (e.g., DELIVERED, IN_TRANSIT)
├── models
│   ├── customer.py          # Defines the Customer class
│   ├── package.py           # Defines the Package class
│   ├── shipment.py          # Defines the Shipment class
│   ├── airline.py           # Defines the AirLine class
│   └── address.py           # Defines the Address class (used in Shipments)
├── tests
│   └── test_*.py            # Unit tests for the code
└── README.md                # Project documentation

```
## Requirements
- Python 3.8+
- unittest (for running unit tests)

##  Running Unit Tests
Unit tests for the code are provided in the tests folder. You can run the tests using the unittest framework. Make sure to navigate to the root directory of the project and run:
```python -m unittest discover -s tests```

