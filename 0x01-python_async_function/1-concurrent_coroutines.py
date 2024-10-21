#!/usr/bin/env python3
"""Implementation of a simple concurrent program using coroutines."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Return a list of all the delays """
    sorted_tasks = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed = asyncio.as_completed(tasks)
    for task in completed:
        result = await task
        sorted_tasks.append(result)
    return sorted_tasks  # list of delay of tasks sorted as completed
