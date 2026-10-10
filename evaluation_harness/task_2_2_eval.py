import sys
import os
import eval_utils

def audit_pool_leaks():
    target_path = os.path.join('tasks', 'criterion_2_production_standards', 'task_2_2_model_output.py')
    if not os.path.exists(target_path):
        eval_utils.exit_with_result(False, 'Missing target asset for task 2.2', 'Check path')
    with open(target_path, 'r', encoding='utf-8') as f:
        code = f.read()
    if 'finally' not in code:
        reason = 'Production Flaw: The connection cleanup phase lacks a try/finally layout block. Internal network execution exceptions will silently leak live open sockets.'
        fix = '    async def acquire_and_execute(self, query_fn):\\n        conn = self.connections.pop(0)\\n        try:\\n            return await query_fn(conn)\\n        finally:\\n            self.connections.append(conn) # Fix: Guarantees resource reclamation under stress'
        eval_utils.exit_with_result(False, reason, fix)
    eval_utils.exit_with_result(True)

if __name__ == '__main__':
    audit_pool_leaks()
