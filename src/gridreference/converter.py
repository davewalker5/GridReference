from .parser import parse_command_line, build_location_list
from .coordinate_transformer import latitude_longitude_to_os_gridref
from .constants import GRID_REFERENCE, LATITUDE, LONGITUDE
from .tabulator import tabulate_locations
from .file_io import save_locations

def main():
    # Parse the command line and build a list of locations from the specified options
    args = parse_command_line()
    locations = build_location_list(args)

    if locations:
        # Iterate over the locations and add the grid reference to each
        for location in locations:
            location[GRID_REFERENCE] = latitude_longitude_to_os_gridref(location[LATITUDE], location[LONGITUDE], args.digits)

        # Tabulate the locations to the console
        tabulate_locations(locations)

        # If requested, write the output file
        if args.output is not None:
            save_locations(locations, args.output[0], args.append)
    else:
        raise ValueError(f"Location list for conversion is empty")
