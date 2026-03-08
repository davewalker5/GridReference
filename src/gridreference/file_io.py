import json
import csv
from pathlib import Path
from .constants import NAME, LATITUDE, LONGITUDE, GRID_REFERENCE


def load_locations(filepath):
    """
    Load a set of location names and coordinates from a CSV or JSON format file
    
    :param filepath: Path to the file to load
    :return: List of loaded location dictionaries
    """
    locations = []

    # Extract the extension
    extension = Path(filepath).suffix.casefold()

    # Load from a JSON format file
    if extension == ".json":
        with open(filepath, "r") as file:
            locations = locations + json.load(file)

    # Load from a CSV format file
    if extension == ".csv":
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                locations.append(row)

    return locations


def save_locations(locations, filepath, append):
    """
    Save a set of locations to a CSV or JSON format file
    
    :param locations: List of location dictionaries
    :param filepath: Path to the file to write
    :param append: True to append to the file, False to create/overwrite it
    """
    # If we're appending and the output file exists, load the current locations from
    # the file, first, and produce a combined, de-duplicated and sorted list from that
    # and the list passed to this method
    if append and Path(filepath).exists():
        names = {l[NAME] for l in locations}
        current_locations = [l for l in load_locations(filepath) if l[NAME] not in names]
        locations = sorted(locations + current_locations, key=lambda l: l[NAME])

    # Extract the extension
    extension = Path(filepath).suffix.casefold()

    # Load from a JSON format file
    if extension == ".json":
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(locations, file, indent=2)

    elif extension == ".csv":
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=[NAME, LATITUDE, LONGITUDE, GRID_REFERENCE])
            writer.writeheader()
            writer.writerows(locations)
