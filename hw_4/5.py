#5

import numpy as np


def matrix_func(some_number):
    for i in range(2, some_number):
        if (some_number % i) == 0:
            matrix = np.zeros((i, some_number // i))
            print(f'{i} на {some_number // i}:\n{matrix}\n')


matrix_func(16)