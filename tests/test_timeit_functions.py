from src.timeit_tools import time_my_function
from src.for_loop_functions import for_loop_make_tuple

def test_time_my_function():
    time_my_function(for_loop_make_tuple, n=100_000, precision=10)
