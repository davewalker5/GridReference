#!/usr/bin/env bash

# Deactivate and remove the old virtual environment, if present
echo "Removing existing Virtual Environment, if present ..."
deactivate 2> /dev/null || true
rm -fr venv

# For older versions of MacOS, pip may not find the proj wheel and will build it from source. Set
# the PROJ_DIR manually if it's present on the machine. The following assumes a MacPorts install
# of proj9
if [ -d "/opt/local/lib/proj9" ]; then
    export PROJ_DIR=/opt/local/lib/proj9
fi

# Create a new environment and activate it
echo "Creating new Virtual Environment ..."
python -m venv venv
. venv/bin/activate

# Make sure pip is up to date
pip install --upgrade pip

# Install the requirements
pip install -r requirements.txt
