import cProfile
import re
import io
import pstats
import time

# cProfile.run("list_comprehension_make_tuple()", sort=-1)
pr = cProfile.Profile()
# pr.enable()
# pr.disable()


def profile_function(fn: callable, *args, n=100):
    pr.enable()
    start = time.time()

    for x in range(n):
        fn(*args)

    end = time.time()
    print(f"**total time took {end-start}. Each fn call took on average: {(end-start)/n}")

    pr.disable()
    s = io.StringIO()
    sortby = pstats.SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
