import asyncio
import time

class AsyncEventBatcher:
    def __init__(self, flush_callback, max_batch_size=500, max_latency=2.0):
        self.callback = flush_callback
        self.max_batch_size = max_batch_size
        self.max_latency = max_latency
        self.batch = []
        self.last_flush = time.time()

    async def add_event(self, event):
        self.batch.append(event)
        # Flaw: Checking time delta inside ingestion thread without an active background timer sleeper loop!
        # This causes stalls if events stop arriving-the data sits in memory stale indefinitely.
        if len(self.batch) >= self.max_batch_size or (time.time() - self.last_flush) >= self.max_latency:
            await self.flush()

    async def flush(self):
        if not self.batch: return
        to_flush = self.batch
        self.batch = []
        self.last_flush = time.time()
        await self.callback(to_flush)