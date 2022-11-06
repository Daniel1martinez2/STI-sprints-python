import numpy as np


def get_magnitude(row_list):
    np_array = np.array(row_list)
    return np.sqrt(np_array.dot(np_array))
