import numpy as np


def run(data, percentage, lighten):
    if lighten == "--lighten":
        print(f"Lightening by {percentage} percent...")
        gamma = 1 - percentage / 100
    else:
        print(f"Darkening by {percentage} percent...")
        gamma = 1 + percentage / 100 * 10
    data = ((data / 255) ** gamma) * 255
    return data.astype(np.uint8)