my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
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
    x = 0
    while x < len(my_list):
        new_list.append(tuple([my_list[x], 1]))
        x += 1
    return new_list


def list_comprehension_make_tuple():
    return [tuple([x, 1]) for x in my_list]


def map_make_tuple():
    return list(map(lambda x: tuple([x, 1]), my_list))


# import numpy as np
# return list(map(lambda x : tuple([x, 1]), my_list))

# def np_nditer_make_tuple():

#     # a = np.arange(5)

#     for x in np.nditer(my_list):
#         print(x)

# # vfunc = np.vectorize(lambda x : tuple([x, 1]), my_list)
# # print(vfunc)
