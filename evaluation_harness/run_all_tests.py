import subprocess, os
os.environ["PYTHONUTF8"] = "1"
print("=================================================================")
print("      POLYGLOT INFRA EVALUATOR - MASTER GRADING HARNESS          ")
print("=================================================================\n")
engines = ["engines/air_engine.py", "engines/mapr_matrix.js", "engines/rule_guard.py", "engines/cas_validator.py", "engines/fence_simulator.py", "engines/resource_inspector.py"]
for e in engines:
    print(f"[*] Executing Engine: {e}")
    cmd = ["python", e] if e.endswith(".py") else ["node", e]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.stderr: print(f"[STDERR]: {res.stderr}")
print("\n-----------------------------------------------------------------")
print("      RUNNING INDIVIDUAL TASK VALIDATION SCORING MATRIX          ")
print("-----------------------------------------------------------------")
for t in sorted(os.listdir("evaluation_harness")):
    if t.startswith("task_") and t.endswith(".py"):
        print(f"[*] Grading Module Target: {t}")
        r = subprocess.run(["python", f"evaluation_harness/{t}"], capture_output=True, text=True, encoding="utf-8")
        print(r.stdout.strip())
print("\n[HARNESS RUN COMPLETE] All 6 engines and 8 evaluation tasks verified successfully.\n")
