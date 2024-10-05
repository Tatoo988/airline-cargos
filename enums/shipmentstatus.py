from enum import Enum
class ShipmentStatus(Enum):
    RECEIVED = 1
    IN_TRANSIT = 2
    DELIVERED = 3
    CANCELLED = 4