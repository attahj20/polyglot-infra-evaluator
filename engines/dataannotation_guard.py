import re, time
print("=== DATAAANNOTATION-TAILORED RULE-COMPLIANCE GUARD (CRAG) ===")
def evaluate_formatting_adherence(label, target_text):
    print(f"\n[*] Auditing fine-grained string syntax on: [{label}]")
    time.sleep(0.3)
    has_markdown_tables = "|" in target_text and "-" in target_text
    has_forbidden_phrases = "vibe-coding" in target_text.lower() or "naively" in target_text.lower()
    if not has_markdown_tables:
        print("       [CRAG ASSERT] ❌ RULE VIOLATION: Model failed to render scannable comparisons via Markdown Tables.")
    if has_forbidden_phrases:
        print("       [CRAG ASSERT] ❌ CONSTRAINT VIOLATION: Banned semantic buzzwords intercepted in text body.")
    if has_markdown_tables and not has_forbidden_phrases:
        print("       [CRAG ASSERT] ✅ 100% PASS: Model response strictly adheres to fine-grained presentation directives.")
bad_response = "The model naively constructs a baseline, vibe-coding its framework logic outside a lock layer."
good_response = "| Vector | Status |\n|---|---|\n| Race Safety | Sequentially Bounded |"
evaluate_formatting_adherence("Non-Compliant LLM Output", bad_response)
evaluate_formatting_adherence("Pristine High-Adherence Output", good_response)
