#!/bin/bash
# Auto-register 7 lobster team agents on Star-Office-UI startup
BASE="http://127.0.0.1:19000"
KEY="lobster_team_2026"

AGENTS=(
  'Sky 🌤️|writing|Star-Office-UI 多agent改造'
  'K哥 📋|researching|10分钟监管巡查'
  'Pin哥 📌|syncing|团队协调'
  'Max 🔧|executing|nginx部署'
  '波哥 🌊|writing|后端WebSocket开发'
  'Jr 🎨|idle|等待F2任务'
  'Yang 🧪|researching|QA测试用例准备'
)

for entry in "${AGENTS[@]}"; do
  IFS='|' read -r name state detail <<< "$entry"
  # Check if already registered
  existing=$(curl -s "$BASE/agents" | python3 -c "
import json,sys
agents=json.load(sys.stdin)
for a in agents:
    if a.get('name','').startswith('${name%%' '*}'):
        print(a['agentId'])
        break
" 2>/dev/null)
  
  if [ -n "$existing" ]; then
    echo "Already registered: $name ($existing)"
    # Push fresh state
    curl -s -X POST "$BASE/agent-push" -H "Content-Type: application/json" \
      -d "{\"agentId\":\"$existing\",\"state\":\"$state\",\"detail\":\"$detail\"}" > /dev/null
  else
    echo "Registering: $name"
    curl -s -X POST "$BASE/join-agent" -H "Content-Type: application/json" \
      -d "{\"name\":\"$name\",\"state\":\"$state\",\"detail\":\"$detail\",\"joinKey\":\"$KEY\"}" | python3 -m json.tool
  fi
done

echo "Done! All agents registered."
