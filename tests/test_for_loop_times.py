import timeit
from src.for_loop_functions import *
import pytest

@pytest.mark.skip(reason="Don't need to test every time.")
def test_for_loop_times():
    assert (
        for_loop_make_tuple()
        == list_comprehension_make_tuple()
        == map_make_tuple()
        == for_loop_with_range_make_tuple()
        == while_loop_make_tuple()
        == for_loop_w_enumerate_make_tuple()
    )

    print(f"for loop:\t\t\t\t{timeit.timeit(for_loop_make_tuple, number=count, globals=globals())/count}")
    print(f"for loop w/ range:\t\t\t{timeit.timeit(for_loop_with_range_make_tuple, number=count, globals=globals())/count}")
    print(
        f"for loop w/ enumerate:\t\t\t{timeit.timeit(for_loop_w_enumerate_make_tuple, number=count, globals=globals())/count}"
    )
    print(f"while loop:\t\t\t\t{timeit.timeit(while_loop_make_tuple, number=count, globals=globals())/count}")
    print(f"list comprehension:\t\t\t{timeit.timeit(list_comprehension_make_tuple, number=count, globals=globals())/count}")
    print(f"map:\t\t\t\t\t{timeit.timeit(map_make_tuple, number=count, globals=globals())/count}")
    # list(map(lambda x: tuple([x, 1]), my_list))
