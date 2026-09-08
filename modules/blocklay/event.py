import asyncio


class Event(asyncio.Event):
    def __init__(self):
        super().__init__()
        self._tsf = asyncio.ThreadSafeFlag()
        event_loop = asyncio.get_event_loop()
        event_loop.create_task(self._run())

    async def _run(self):
        while True:
            await self._tsf.wait()
            super().set()

    def set(self):
        self._tsf.set()
