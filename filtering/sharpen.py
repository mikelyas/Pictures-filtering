import numpy as np

sharpening_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0],
])

def run(data):
    print("Sharpening...")
    return apply_filter(data, sharpening_kernel)


def matrix_extention(a, times_to_extend):
    for i in range(times_to_extend):
        a = np.insert(a, 0, 0, 0)
        a = np.insert(a, len(a), 0, 0)
        a = np.insert(a, 0, 0, 1)
        a = np.insert(a, len(a[0]), 0, 1)
    return a

def padding(image_chaged, kernel, height, width):
    list_tmp = []
    for i in range(height):
        for j in range(width):
            c = kernel * image_chaged[i:i + len(kernel), j:j + len(kernel[0])]
            list_tmp.append(np.sum(c))

    res = np.array(list_tmp)
    res = res.reshape([height, width])
    return res


def apply_filter(image: np.array, kernel: np.array) -> np.array:
    # A given image has to have either 2 (grayscale) or 3 (RGB) dimensions
    assert image.ndim in [2, 3]
    # A given filter has to be 2 dimensional and square
    assert kernel.ndim == 2
    assert kernel.shape[0] == kernel.shape[1]
    #extend matrix with nulls
    times_to_extend = int((len(kernel) - 1) / 2)
    image_tmp = np.empty([len(image) + times_to_extend * 2, len(image[0]) + times_to_extend * 2]) if image.ndim == 2 else np.empty([len(image) + times_to_extend * 2, len(image[0]) + times_to_extend * 2, 3])
    if image.ndim == 2:
        image_tmp = matrix_extention(image, times_to_extend)
    else:
        for i in range(3):
            image_tmp[:, :, i] = matrix_extention(image[:, :, i], times_to_extend)

    #padding
    new_image = np.copy(image)
    height = len(image)
    width = len(image[0])
    if image.ndim == 2:
        new_image = padding(image_tmp, np.rot90(kernel, 2, axes=(0, 1)), height, width)
    else:
        for i in range(3):
            new_image[:, :, i] = padding(image_tmp[:, :, i], np.rot90(kernel, 2, axes=(0, 1)), height, width)

    return new_image
