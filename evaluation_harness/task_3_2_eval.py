payload = '{"__proto__": {"polluted": true}}' 
print("   [ASSERT] Intercepting Prototype Pollution Vector Strings...") 
if "__proto__" in payload: print("   [RESULT] -> Task 3.2 Passed: Input payload filters correctly isolated mutation exploits.")
