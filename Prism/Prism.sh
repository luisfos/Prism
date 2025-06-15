#!/bin/bash

PRISM_ROOT="$(dirname "$(readlink -f "$0")")"

python3 $PRISM_ROOT/Scripts/PrismTray.py
