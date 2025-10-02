from dataclasses import dataclass
import subprocess

@dataclass(slots=True, frozen=True)
class Coordinates():
    longitude: float
    latitude: float

def get_gps_coordinates() -> Coordinates:
    """returns current coordinates using external service"""
    coords_from_curl = _get_coords_from_curl()
    gps_coords = _parse_coords(coords_from_curl)

    return gps_coords

def _get_coords_from_curl() -> bytes:
    command = 'curl ipinfo.io/loc'
    captured_output = subprocess.run(command, capture_output=True).stdout
    return captured_output

def _parse_coords(output: bytes) -> Coordinates:
    splitted_output = output.decode().split(',')
    return Coordinates(
        longitude=float(splitted_output[0]),
        latitude=float(splitted_output[1])
    )

if __name__ == "__main__":
    print(get_gps_coordinates())