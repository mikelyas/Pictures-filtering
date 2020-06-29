import sys
sys.path.append(sys.path[0][:-5])
import numpy as np
from PIL import Image, ImageOps
from numpy.testing import assert_equal
from pytest import fixture
from filtering import bw, inverse, rotate, mirror


@fixture
def image():
    return Image.open("./lenna.png")


def test_bw(image):
    assert bw.run(np.asarray(image)).ndim == 2


def test_inverse(image):
    original = Image.open("./lenna.png").convert("RGB")
    assert_equal(np.asarray(ImageOps.invert(original)), inverse.run(np.asarray(image)))


def test_rotate(image):
    assert_equal(np.asarray(Image.open("./lenna.png").rotate(270)), rotate.run(np.asarray(image)))


def test_mirror(image):
    assert_equal(np.asarray(ImageOps.mirror(Image.open("./lenna.png"))), mirror.run(np.asarray(image)))
