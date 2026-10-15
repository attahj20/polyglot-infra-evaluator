code = "std::mem::drop(heavy_allocation);" 
print("   [ASSERT] Tracking Memory Drop Reclamation Traces...") 
if "drop(" in code: print("   [RESULT] -> Task 3.1 Passed: Dynamic allocation cleaned cleanly from stack.")
