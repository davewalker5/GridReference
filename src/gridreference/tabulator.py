from .constants import NAME, LATITUDE, LONGITUDE, GRID_REFERENCE
from .constants import NAME_WIDTH, LATITUDE_WIDTH, LONGITUDE_WIDTH, GRID_REFERENCE_WIDTH


def _print_row(values, column_widths):
    """
    Tabulate a set of values as a table row with given column widths. Floating point
    numbers are formatted to 2 decimal places

    :param values: List of alues to tabulate
    :param column_widths: List of integer column widths to pad each column to
    """
    for i, value in enumerate(values):
        if isinstance(value, float):
            value_string = f"{value:.6f}".ljust(column_widths[i])
        else:
            value_string = str(value).ljust(column_widths[i])

        print(f"| {value_string[:column_widths[i]]} ", end='')

    print("|")


def _print_separator(column_widths):
    """
    Print the separator between header and table body

    :param column_widths: List of column widths
    """
    row = ["+"]
    for width in column_widths:
        row.append("-" * (2 + width))
        row.append("+")

    print("".join(row))


def tabulate_locations(locations):
    """
    Tabulate a collection of location dictionaries in the current window

    :param locations: List of location dictionaries to tabulate
    """
    headers = [NAME, LATITUDE, LONGITUDE, GRID_REFERENCE]
    widths = [NAME_WIDTH, LATITUDE_WIDTH, LONGITUDE_WIDTH, GRID_REFERENCE_WIDTH]
    _print_row(headers, widths)
    _print_separator(widths)
    for location in locations:
        row_data = [location[NAME], location[LATITUDE], location[LONGITUDE], location[GRID_REFERENCE]]
        _print_row(row_data, widths)
