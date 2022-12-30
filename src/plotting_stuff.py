from matplotlib import pyplot as plt

# from functools import partial
import random
from collections import defaultdict


number_counter = defaultdict(lambda: 0)
random_set_of_numbers = random.sample(range(1, 101), 100)
# random_set_of_numbers = random.sample(['red', 'blue'], counts=[4,3], k=7)

# print(random_set_of_numbers)
for num in random_set_of_numbers:
    number_counter[num] += 1

plt.rcParams["figure.figsize"] = [11, 11]
plt.rcParams["figure.autolayout"] = True
# x = [4]
# y = [3]
plt.xlim(0, 105)
plt.ylim(0, 102)
plt.grid()
plt.bar(range(1, 101), number_counter.keys())
# my_plotter = partial(plt.plot, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="red")
# my_plotter(x,y)
# my_plotter([5],[5])
# plt.plot(x, y, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="red")
plt.show()
