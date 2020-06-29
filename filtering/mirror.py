import numpy as np


def run(data):
    print("Applying mirror...")
    return np.flip(data, 1)