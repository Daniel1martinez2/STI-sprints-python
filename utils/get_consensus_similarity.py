import pandas as pd
import numpy as np
from utils.row_frame_to_list import row_frame_to_list
from utils.get_magnitude import get_magnitude
from utils.dot_product import dot_product

"""
    Data Frame as input
"""


def get_consensus_similarity(DF_A, DF_B):

    # Convert each data frame rows to number list
    row_list_A = row_frame_to_list(DF_A)
    row_list_B = row_frame_to_list(DF_B)

    # Dot product
    dot_product_data = dot_product(row_list_A, row_list_B)

    # Magnitudes
    magnitude_A = get_magnitude(row_list_A)
    magnitude_B = get_magnitude(row_list_B)
    return (dot_product_data / (magnitude_A * magnitude_B))*100
