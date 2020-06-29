import numpy as np


def run(data):
    print("BW...")
    if data.ndim == 2:
        return data
    return np.mean(data, axis=2).astype(np.uint8)