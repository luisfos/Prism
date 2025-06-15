#!/usr/bin/env python3
import os
import sys
import subprocess

# Get the root directory of the project
PRISM_ROOT = os.path.dirname(os.path.abspath(__file__))

# set PRISM_DEBUG environment variable if not already set
if "PRISM_DEBUG" not in os.environ:
    os.environ["PRISM_DEBUG"] = "1"

# Path to the PrismTray.py script
prism_tray = os.path.join(PRISM_ROOT, "Scripts", "PrismTray.py")

if not os.path.exists(prism_tray):
    print(f"Error: {prism_tray} not found.")
    sys.exit(1)

# Run the PrismTray.py script
subprocess.run([sys.executable, prism_tray] + sys.argv[1:])
