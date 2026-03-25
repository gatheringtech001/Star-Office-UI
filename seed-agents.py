"""Seed team agents into agents-state.json on every startup."""
import json, os
from datetime import datetime, timedelta

STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agents-state.json")

TEAM_AGENTS = [
    {"agentId": "sky", "name": "Sky 🌤️", "state": "writing", "detail": "前端开发中", "area": "writing"},
    {"agentId": "manager", "name": "K哥 📋", "state": "writing", "detail": "项目管理中", "area": "writing"},
    {"agentId": "cto", "name": "Pin哥 📌", "state": "writing", "detail": "技术架构中", "area": "writing"},
    {"agentId": "devops", "name": "Max 🔧", "state": "writing", "detail": "运维部署中", "area": "writing"},
    {"agentId": "backend", "name": "波哥 🌊", "state": "writing", "detail": "后端开发中", "area": "writing"},
    {"agentId": "frontend", "name": "Jr 🎨", "state": "idle", "detail": "休息中", "area": "breakroom"},
    {"agentId": "qa", "name": "Yang 🧪", "state": "writing", "detail": "QA测试中", "area": "writing"},
]

def seed():
    agents = []
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE) as f:
                agents = json.load(f)
        except:
            agents = []
    
    existing_ids = {a.get("agentId") for a in agents}
    now = datetime.now()
    
    for t in TEAM_AGENTS:
        if t["agentId"] not in existing_ids:
            agents.append({
                **t,
                "isMain": True,
                "source": "seed",
                "joinKey": None,
                "authStatus": "approved",
                "authExpiresAt": (now + timedelta(days=365)).isoformat(),
                "lastPushAt": now.isoformat(),
                "updated_at": now.isoformat(),
            })
            print(f"  Seeded: {t['name']}")
        else:
            # Refresh lastPushAt to prevent auto-offline
            for a in agents:
                if a.get("agentId") == t["agentId"]:
                    a["lastPushAt"] = now.isoformat()
                    if not a.get("authExpiresAt") or datetime.fromisoformat(a["authExpiresAt"]) < now:
                        a["authExpiresAt"] = (now + timedelta(days=365)).isoformat()
                    break
    
    with open(STATE_FILE, "w") as f:
        json.dump(agents, f, ensure_ascii=False, indent=2)
    print(f"  Total agents: {len(agents)}")

if __name__ == "__main__":
    print("Seeding team agents...")
    seed()
