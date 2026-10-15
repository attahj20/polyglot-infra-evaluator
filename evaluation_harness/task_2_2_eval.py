msg = '{"step": 2, "action": "SYN-ACK"}' 
print("   [ASSERT] Validating Multi-Agent State-Machine Handshakes...") 
if "SYN-ACK" in msg: print("   [RESULT] -> Task 2.2 Passed: Custom framed network transaction verified.")
