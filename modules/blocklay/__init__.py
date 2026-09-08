import asyncio

from .event import Event

__all__ = ("call", "stop", "task", "broadcast", "start", "shutdown", "Event")

_task_groups = None
_event_groups = None

asyncio.new_event_loop()


def call(task_script, task_group_name=None):
    event_loop = asyncio.get_event_loop()
    global _task_groups
    if _task_groups is None:
        _task_groups = {}

    if task_group_name is None:
        task_group_name = task_script.__globals__["__file__"]
    task_group = _task_groups.setdefault(task_group_name, [])
    task_group.append(event_loop.create_task(task_script()))


def stop(task_group_name):
    if _task_groups is not None:
        task_group = _task_groups.setdefault(task_group_name, [])
        current_task = asyncio.current_task()
        for task in task_group:
            if task is not current_task:
                task.cancel()
        task_group.clear()
        task_group.append(current_task)


def event_task(event_name):
    global _event_groups
    if _event_groups is None:
        _event_groups = {}

    def task(task_script):
        event = _event_groups.setdefault(event_name, Event())

        async def script():
            while True:
                await event.wait()
                call(task_script)
                await asyncio.sleep_ms(1)
                event.clear()

        call(script, "blocklay")

    return task


def flag_task(flag):
    def task(task_script):
        async def script():
            while True:
                if await flag():
                    call(task_script)
                await asyncio.sleep_ms(5)

        call(script, "blocklay")

    return task


def task(event_flag=None):
    if type(event_flag) is str:
        return event_task(event_flag)

    if callable(event_flag):
        return flag_task(event_flag)

    return call


def reset():
    event_loop = asyncio.get_event_loop()
    event_loop.stop()
    event_loop.close()

    global _task_groups, _event_groups
    if _task_groups is not None:
        _task_groups.clear()
        _task_groups = None

    if _event_groups is not None:
        _event_groups.clear()
        _event_groups = None


def start():
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_forever()
    except KeyboardInterrupt:
        print("Shutdown, Bye!")
    finally:
        reset()


def shutdown():
    raise KeyboardInterrupt


def broadcast(event):
    if type(event) is str:
        event = _event_groups.setdefault(event, Event())
    event.set()
