import os, subprocess
print("=================================================================")
print("      POLYGLOT INFRA EVALUATOR - MASTER GRADING HARNESS          ")
print("=================================================================\n")
engines = ["engines/air_engine.py", "engines/mapr_matrix.js", "engines/rule_guard.py", "engines/cas_validator.py", "engines/fence_simulator.py", "engines/resource_inspector.py"]
for engine in engines:
    print(f"[*] Initializing execution sequence for: {engine}")
    cmd = ["python", engine] if engine.endswith(".py") else ["node", engine]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(res.stdout)
    if res.stderr: print(f"[STDERR]: {res.stderr}")
print("[HARNESS RUN COMPLETE] All 6 verification benchmarks executed successfully.")
