import sys
import os
import eval_utils

def audit_js_memory_leaks():
    target_path = os.path.join('tasks', 'criterion_2_production_standards', 'task_2_3_model_output.js')
    if not os.path.exists(target_path):
        eval_utils.exit_with_result(False, 'Missing target asset for task 2.3', 'Check path')
    with open(target_path, 'r', encoding='utf-8') as f:
        code = f.read()
    if 'removeListener' not in code and 'off' not in code:
        reason = 'Production Flaw: The component lifecycle hooks lack listener unbinding logic.'
        fix = '    mount() { this.listener = (d) => { }; metricsStream.on(---packet---, this.listener); }\n    unmount() { metricsStream.off(---packet---, this.listener); }'.replace('---', chr(39))
        eval_utils.exit_with_result(False, reason, fix)
    eval_utils.exit_with_result(True)

if __name__ == '__main__':
    audit_js_memory_leaks()