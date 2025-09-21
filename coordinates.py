from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Coordinates():
    latitude: float
    longitude: float

def get_gps_coordinates() -> Coordinates:
    """returns current coordinates using external service"""
    return Coordinates(10, 20)