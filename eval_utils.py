import sys
import json

def exit_with_result(success, error_message="", expected_fix=""):
    """
    Handles standardized exits for the workspace scanner.
    If it fails, it prints a structured JSON block for the PowerShell utility to parse.
    """
    if success:
        print("OK")
        sys.exit(0)
    else:
        result = {
            "status": "Logic Mismatch",
            "reason": error_message,
            "suggested_fix": expected_fix
        }
        # Print with a special prefix so the PowerShell scanner can extract it cleanly
        print(f"__EVAL_FIX_DATA__:{json.dumps(result)}")
        sys.exit(1)
