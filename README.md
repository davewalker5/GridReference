# GridReference

[![GitHub issues](https://img.shields.io/github/issues/davewalker5/GridReference)](https://github.com/davewalker5/GridReference/issues)
[![Releases](https://img.shields.io/github/v/release/davewalker5/GridReference.svg?include_prereleases)](https://github.com/davewalker5/GridReference/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/davewalker5/GridReference/blob/master/LICENSE)
[![Language](https://img.shields.io/badge/language-python-blue.svg)](https://www.python.org)
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/davewalker5/GridReference)](https://github.com/davewalker5/GridReference/)

## Overview

The grid reference converter is a command-line application that takes pairs of location coordinates (latitude, longitude) for UK locations and converts them to the corresponding Ordnance Survay grid reference.

Input coordinates may be supplied as:

- A CSV file, specifying a collection of 1 or more locations
- A JSON file, specifying a collection of 1 or more locations
- An add-hoc coorindate specified on the command line

Output is to the terminal window running the application and to a CSV or JSON format file.

## Setting Up and Running the Application

From the root of the project, enter the following command to build the Python virtual environment:

```bash
./scripts/make_venv.sh
```

Then, to run the converter for an ad-hoc location use the following:

```bash
./scripts/run_converter.sh -c latitude longitude -n name
```

For example:

```bash
./scripts/run_converter.sh -c 50.0664 -5.7147 -n "Land's End"
```

The output will look similar to the following:

```
| Name                           | Latitude   | Longitude  | Grid Reference  |
+--------------------------------+------------+------------+-----------------+
| Land's End                     | 50.066400  | -5.714700  | SW 342 250      |
```

## Command Line Options

| Option        | Short Form | Arguments          | Default                    | Purpose                                                            |
| ------------- | ---------- | ------------------ | -------------------------- | ------------------------------------------------------------------ |
| --coordinates | -c         | latitude longitude | N/A                        | Latitude and longitude for an ad-hoc location                      |
| --name        | -n         | name               | Ad Hoc YYYY-MM-DD HH:MM:SS | Name an ad-hoc location                                            |
| --input       | -i         | filepath           | N/A                        | Path to a CSV/JSON file containing location definitions            |
| --output      | -o         | filepath           | N/A                        | Path for a CSV/JSON file where the results will be written         |
| --append      | -a         | N/A                | N/A                        | If specified, append to the output file rather than overwriting it |
| --digits      | -d         | digits             | 6                          | Number of digits to include in grid references (6, 8 or 10)        |

## File Formats

### Input CSV Format

Input CSV files should contain columns for the Name, Latitude and Longitude of each location. Case of the column titles is significant:

```csv
Name,Latitude,Longitude
John o'Groats,58.6373,-3.0689
Land's End,50.0664,-5.7147
```

### Input JSON Format

Input JSON files should specify a list of dictionaries, one per location, in which there are Name, Latitude and Longitude properties. Case of the property names is significant:

```json
[
  {
    "Name": "John o'Groats",
    "Latitude": "58.6373",
    "Longitude": "-3.0689"
  },
  {
    "Name": "Land's End",
    "Latitude": "50.0664",
    "Longitude": "-5.7147"
  }
]
```

### Output File Format

Output CSV files are identical to the input CSV format with the addition of a column for the grid reference:

```csv
Name,Latitude,Longitude,Grid Reference
John o'Groats,58.6373,-3.0689,ND 380 726
Land's End,50.0664,-5.7147,SW 342 250
```

Output JSON files are identical to the input JSON format with the addition of a property for the grid reference:

```json
[
  {
    "Name": "John o'Groats",
    "Latitude": "58.6373",
    "Longitude": "-3.0689",
    "Grid Reference": "ND 380 726"
  },
  {
    "Name": "Land's End",
    "Latitude": "50.0664",
    "Longitude": "-5.7147",
    "Grid Reference": "SW 342 250"
  }
]
```

# Authors

- **Dave Walker** - _Initial work_

# Feedback

To file issues or suggestions, please use the [Issues](https://github.com/davewalker5/GridReference/issues) page for this project on GitHub.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
