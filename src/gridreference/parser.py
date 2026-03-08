import argparse
from datetime import datetime
from .constants import PROGRAM_NAME, PROGRAM_VERSION, PROGRAM_DESCRIPTION
from .file_io import load_locations


def _configure_parser():
    """
    Configure the command line parser

    :return: Configured parser object
    """
    parser = argparse.ArgumentParser(
        prog=f"{PROGRAM_NAME} v{PROGRAM_VERSION}",
        description=PROGRAM_DESCRIPTION
    )

    parser.add_argument("-c", "--coordinates", nargs=2, type=float, help="Latitude and longitude for a location")
    parser.add_argument("-n", "--name", nargs=1, help="Supply a name for an ad-hoc location")
    parser.add_argument("-i", "--input", nargs=1, help="Path to a CSV/JSON file containing location definitions")
    parser.add_argument("-o", "--output", nargs=1, help="Path for a CSV/JSON file where the results will be written")
    parser.add_argument("-a", "--append", action="store_true", help="Append to the output file rather than overwriting it")
    parser.add_argument("-d", "--digits", type=int, default=6, help="Number of digits to include in grid references")

    return parser


def parse_command_line():
    """
    Configure the command line parser and parse the command line

    :return: Arguments dictionary resulting from parsing the command line
    """
    parser = _configure_parser()
    args = parser.parse_args()

    return args


def build_location_list(args):
    """
    Build a list of location latitudes and longitudes based on the command line options

    :param args: Command line options
    :return: List of location dictionaries
    """
    locations = []

    # Add an add-hoc location
    if args.coordinates is not None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        name = args.name[0] if args.name else f"Ad Hoc {timestamp}"
        locations.append({
            "Name": name,
            "Latitude": float(args.coordinates[0]),
            "Longitude": float(args.coordinates[1])
        })

    # Load locations defined in an input file
    if args.input is not None:
        locations = locations + load_locations(args.input[0])

    # Sort the locations
    locations = sorted(locations, key=lambda x: x["Name"])
    return locations
