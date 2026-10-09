import asyncio
import logging

class AsyncConnectionPool:
    def __init__(self, pool_size=10):
        self.pool_size = pool_size
        self.connections = [f'Conn-{i}' for i in range(pool_size)]

    async def acquire_and_execute(self, query_fn):
        if not self.connections:
            raise Exception('Pool exhausted')
        conn = self.connections.pop(0)
        result = await query_fn(conn)
        self.connections.append(conn)
        return result