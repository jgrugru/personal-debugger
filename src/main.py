# import timeit
# import numpy as np
my_list = [1,2,3,4,5,6,7,8,9,10]
count = 1_000_000

def for_loop_make_tuple():
    new_list = []
    for x in my_list:
        new_list.append(tuple([x, 1]))
    return new_list

def for_loop_w_enumerate_make_tuple():
    new_list = []
    for i, x in enumerate(my_list):
        new_list.append(tuple([x, 1]))
    return new_list

def for_loop_with_range_make_tuple():
    new_list = []
    for x in range(len(my_list)):
        new_list.append(tuple([my_list[x], 1]))
    return new_list

def while_loop_make_tuple():
    new_list = []
    x  = 0
    while x < len(my_list):
        new_list.append(tuple([my_list[x], 1]))
        x += 1
    return new_list

def list_comprehension_make_tuple():
    return [tuple([x, 1]) for x in my_list]

def map_make_tuple():
    return list(map(lambda x : tuple([x, 1]), my_list))

# def np_nditer_make_tuple():

#     # a = np.arange(5)

#     for x in np.nditer(my_list):
#         print(x)

# # vfunc = np.vectorize(lambda x : tuple([x, 1]), my_list)
# # print(vfunc)
# assert for_loop_make_tuple() == list_comprehension_make_tuple() == map_make_tuple() == for_loop_with_range_make_tuple() == while_loop_make_tuple() == for_loop_w_enumerate_make_tuple()

# print(f"for loop:\t\t\t\t{timeit.timeit(for_loop_make_tuple, number=count, globals=globals())/count}")
# print(f"for loop w/ range:\t\t\t{timeit.timeit(for_loop_with_range_make_tuple, number=count, globals=globals())/count}")
# print(f"for loop w/ enumerate:\t\t\t{timeit.timeit(for_loop_w_enumerate_make_tuple, number=count, globals=globals())/count}")
# print(f"while loop:\t\t\t\t{timeit.timeit(while_loop_make_tuple, number=count, globals=globals())/count}")
# print(f"list comprehension:\t\t\t{timeit.timeit(list_comprehension_make_tuple, number=count, globals=globals())/count}")
# print(f"map:\t\t\t\t\t{timeit.timeit(map_make_tuple, number=count, globals=globals())/count}")
# # list(map(lambda x : tuple([x, 1]), my_list))

import cProfile
import re
import io
import pstats
import time
# cProfile.run('list_comprehension_make_tuple()', sort=-1)
# cProfile.run('re.compile("foo|bar")', sort=-1)


pr = cProfile.Profile()
# pr.enable()
# # for_loop_make_tuple()
# re.compile("foo|bar")
# pr.disable()


# def profile_function(fn: callable, *args, n=100):
#     # pr.enable()
#     start = time.time()

#     for x in range(n):
#         fn(*args)

#     end = time.time()
#     print(f"**total time took {end-start}. Each fn call took on average: {(end-start)/n}")


    # pr.disable()
    # s = io.StringIO()
    # sortby = pstats.SortKey.CUMULATIVE
    # ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    # ps.print_stats()
    # print(s.getvalue())


# profile_function(for_loop_make_tuple)

from typing import Callable

def time_my_function(fn: Callable, *args, n=100) -> tuple[float, float]:
    """Timing function\n
    Provides total time and average time for fn call. Runs the given function n times, default 100.
    Returns a tuple of (total_time_ran, avg_time_per_fn_call)."""
    start = time.time()
    for x in range(n):
        fn(*args)
    end = time.time()
    print(f"{__file__}-----{fn.__name__}-----:")
    print(f"\t- The fn ran {n} times for a total of: {end-start}.\n\t- Each fn call took on average: {(end-start)/n}")
    return (end-start, (end-start)/n)

time_my_function(for_loop_make_tuple)
