import sys
import os
import eval_utils

def audit_rust_memory_standards():
    target_path = os.path.join('tasks', 'criterion_2_production_standards', 'task_2_1_model_output.rs')
    if not os.path.exists(target_path):
        eval_utils.exit_with_result(False, 'Missing target asset for task 2.1', 'Check path')
    with open(target_path, 'r', encoding='utf-8') as f:
        code = f.read()
    if 'Ordering::Relaxed' in code:
        reason = 'Production Flaw: Model used Relaxed atomic ordering on global state counters. This permits compiler reordering, which violates absolute synchronization consistency across microservice threads.'
        fix = '    pub fn increment_success(&self) {\\n        // Fix: Upgrade memory ordering barriers to Release/Acquire or Sequential Consistency\\n        self.total_processed.fetch_add(1, Ordering::SeqCst);\\n    }'
        eval_utils.exit_with_result(False, reason, fix)
    eval_utils.exit_with_result(True)

if __name__ == '__main__':
    audit_rust_memory_standards()