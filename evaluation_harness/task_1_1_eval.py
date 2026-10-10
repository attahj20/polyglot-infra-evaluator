import sys
import os
import eval_utils

def audit_rust_limiter():
    print('Auditing Task 1.1: Rust TokenBucket Capacity Extension...')
    target_path = os.path.join('tasks', 'criterion_1_vibe_coding', 'task_1_1_model_output.rs')
    if not os.path.exists(target_path):
        eval_utils.exit_with_result(False, f'Missing target asset at: {target_path}', 'Check paths')
    with open(target_path, 'r', encoding='utf-8') as f:
        code = f.read()
    if 'tokens.load' in code and 'tokens.store' in code:
        reason = 'Production Flaw: The model used separate load and store statements on tokens creating a TOCTOU race.'
        fix = '   pub fn try_update_capacity(&self, new_capacity: u64) -> Result<(), &str> {\\n       // Use atomic CAS loop structure here\\n   }'
        eval_utils.exit_with_result(False, reason, fix)
    eval_utils.exit_with_result(True)

if __name__ == '__main__':
    audit_rust_limiter()