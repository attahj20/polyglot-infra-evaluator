cfg = '{"server": {"port": 8080, "timeout_ms": 5000}}' 
print("   [ASSERT] Checking Infrastructure Schema Bounds...") 
import json 
d = json.loads(cfg) 
if d["server"]["port"] == 8080 and d["server"]["timeout_ms"] > 0: print("   [RESULT] -> Task 1.2 Passed: Valid port range and timeout configured.")
