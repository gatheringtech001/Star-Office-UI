#!/bin/bash
# Start Star-Office-UI backend + auto-register agents
cd /tmp/Star-Office-UI/backend
python3 app.py &
PID=$!
echo "Backend started (PID $PID)"
sleep 2
bash /tmp/Star-Office-UI/auto-register-agents.sh
echo "Backend running on :19000"
wait $PID
