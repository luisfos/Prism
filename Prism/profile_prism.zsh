#!/bin/zsh
# Profile Prism with py-spy (via uvx) for 20 seconds and output a speedscope file

# Print Python version and location
python3 --version
# echo "python3 location: $(which python3)"

# echo "py-spy profiling is currently commented out."
# py-spy record -s -f speedscope -o prism-profile.speedscope.json -d 20 -- uv run prism.py


uv run prism.py &
PRISM_PID=$!
py-spy record -s -f speedscope -o prism-profile.speedscope.json -d 20 --pid $PRISM_PID
# wait $PRISM_PID

echo "Profiling complete. Open prism-profile.speedscope.json with https://www.speedscope.app/ to view results."
