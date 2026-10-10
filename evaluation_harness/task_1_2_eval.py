import sys
import os
import eval_utils

def audit_async_batcher():
    target_path = os.path.join('tasks', 'criterion_1_vibe_coding', 'task_1_2_model_output.py')
    if not os.path.exists(target_path):
        eval_utils.exit_with_result(False, 'Missing target asset for task 1.2', 'Check path')
    with open(target_path, 'r', encoding='utf-8') as f:
        code = f.read()
    if 'create_task' not in code and 'asyncio.sleep' not in code:
        reason = 'Production Flaw: Ingestion thread timeout checking stalls if active event input stops streaming.'
        fix = '    async def _start_timeout_worker(self):\\n        while True:\\n            await asyncio.sleep(self.max_latency)\\n            await self.flush()'
        eval_utils.exit_with_result(False, reason, fix)
    eval_utils.exit_with_result(True)

if __name__ == '__main__':
    audit_async_batcher()