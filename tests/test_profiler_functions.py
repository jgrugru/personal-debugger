from src.profiling_tools import profile_function
from src.for_loop_functions import for_loop_make_tuple


def test_profile_function():
    profile_function(for_loop_make_tuple)
