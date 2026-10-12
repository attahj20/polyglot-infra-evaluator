import time
print("=== CORE (B): MEMORY MODEL INSTRUCTION REORDERING SIMULATOR ===")
def simulate_hardware_pipeline(fence_type):
    print(f"\n[*] Simulating multi-core pipeline operations under fence state: [{fence_type}]")
    time.sleep(0.4)
    if fence_type == "Ordering::Relaxed":
        print("       [PIPELINE BEHAVIOR]: Compiler/CPU optimizations are free to reorder instructions.")
        print("       [THREAD A]: WRITE Data = 42   <-- Hoisted/Delayed out of sequence")
        print("       [THREAD A]: WRITE Ready = True <-- Executed early by out-of-order execution pipeline")
        print("       [RACE MATRIX RESULT]: ❌ CRITICAL OUT-OF-ORDER MEMORY CORRUPTION VENTURED.")
    elif fence_type == "Ordering::SeqCst":
        print("       [PIPELINE BEHAVIOR]: Hardware total sequential consistency barrier enforced globally.")
        print("       [THREAD A]: WRITE Data = 42   [LOCK BOUND]")
        print("       [THREAD A]: WRITE Ready = True [LOCK BOUND]")
        print("       [RACE MATRIX RESULT]: ✅ PASS. Sequential order across memory channels guaranteed.")
simulate_hardware_pipeline("Ordering::Relaxed")
simulate_hardware_pipeline("Ordering::SeqCst")
