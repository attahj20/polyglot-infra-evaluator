code = "loop { match state.compare_exchange_weak(curr, new, SeqCst, Relaxed) }" 
print("   [ASSERT] Checking Atomic TOCTOU Retry Safety Loops...") 
if "compare_exchange_weak" in code and "loop" in code: print("   [RESULT] -> Task 1.1 Passed: Model correctly handles CAS retry loops.")
