#!/bin/bash

# THIS SCRIPT IS FOR HYPRLAND WM ONLY!

# Get the absolute path of the directory containing linux-dashboard.py
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Set the path to the linux-dashboard.py file
DASHBOARD="${SCRIPT_DIR}/linux-dashboard.py"

# Check if the linux-dashboard.py file exists
if [ ! -f "$DASHBOARD" ]; then
    echo "Error: Cannot find linux-dashboard.py in ${SCRIPT_DIR}"
    exit 1
fi

# Launch the linux dashboard with Hyprland
hyprctl dispatch exec "[float; size 1020 875; center] python3 ${DASHBOARD}"
