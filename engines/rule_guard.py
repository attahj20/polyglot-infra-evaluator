import re, time
print("=== PROJECT 3: DETERMINISTIC RULE-ADHERENCE GUARD ===")
def evaluate_code(label, code_content):
    print(f"\n[*] Evaluating rule adherence metrics on: {label}")
    if re.search(r"Ordering::Relaxed", code_content):
        print("       [SCORE] Failed: Code uses banned Ordering::Relaxed parameters.")
    elif not re.search(r"Ordering::SeqCst", code_content):
        print("       [SCORE] Failed: Missing mandatory Ordering::SeqCst barriers.")
    else:
        print("       [SCORE] Pass. Code strictly matches layout directives.")
evaluate_code("Failing Model Candidate Code", "self.state.fetch_add(1, Ordering::Relaxed);")
evaluate_code("Passing Model Candidate Code", "self.state.fetch_add(1, Ordering::SeqCst);")
