from typing import Callable, List
import time
import statistics
from loguru import logger


def time_my_function(fn: Callable, n: int = 100, precision: int = 6, *args, **kwargs) -> List[float]:
    """
    Timing function\n
    Provides mean, median, stdev, min, and max time for fn call. Runs the given function n times, default 100.
    Returns a list of all run times List[float].
    """
    list_of_times = []
    for x in range(n):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        list_of_times.append(end - start)

    average = round(sum(list_of_times) / n, precision)
    std_dev = round(statistics.stdev(list_of_times), precision)
    minimum = round(min(list_of_times), precision)
    maximum = round(max(list_of_times), precision)

    logger.info(f"{n} times: mean={average}, median={round(statistics.median(list_of_times), precision)}, stdev={std_dev}, min={minimum}, max={maximum}")
    return list_of_times
