# Polyglot Infra Evaluator - Core Execution Harnesses

This section contains the operational documentation and execution instructions for the three primary SWE LLM benchmarking engines running natively on the local system.

---

## Project 1: Autonomous Infrastructure Repair (AIR) Engine

*   **File Path:** engines/air_engine.py
*   **Target Scope:** Evaluates an LLM's capability to intercept live system errors and deploy precise configuration patches without breaking type specifications.
*   **How it Works:** Simulates a broken local server environment with an invalid string port and negative timeouts. It reads a sample LLM candidate patch, runs validation gates, and programmatically applies or rejects the fix.

### How to Run Locally
`powershell
python .\engines\air_engine.py
`

---

## Project 2: Multi-Agent Protocol Rigging (MAPR) Matrix

*   **File Path:** engines/mapr_matrix.js
*   **Target Scope:** Evaluates asynchronous multi-agent coordination, structural framing, and lock-free connection lifecycles over a network matrix.
*   **How it Works:** Spins up a real multi-threaded network server on the local loopback interface (127.0.0.1:9999). It initializes a state machine handshake sequence (SYN -> SYN-ACK -> DATA-TX -> FIN) to verify deterministic connection teardowns.

### How to Run Locally
`powershell
node .\engines\mapr_matrix.js
`

---

## Project 3: Hardened Sandbox Rule Guard (CRAG)

*   **File Path:** engines/rule_guard.py
*   **Target Scope:** Automates strict instruction adherence grading, negative constraint matching, and memory configuration validation.
*   **How it Works:** Uses high-precision Abstract Syntax Tree (AST) token scanning to cross-examine model outputs against explicit security constraints (e.g., blocking Ordering::Relaxed and enforcing Ordering::SeqCst memory boundaries).

### How to Run Locally
`powershell
python .\engines\rule_guard.py
`

---

## Summary of Local Testing Commands
Execute these commands in your PowerShell console to verify the entire evaluator suite performance:
`powershell
# Run Infrastructure Telemetry Test
python .\engines\air_engine.py

# Run Async Handshake Simulation
node .\engines\mapr_matrix.js

# Run Code Layout Constraint Scanner
python .\engines\rule_guard.py
`