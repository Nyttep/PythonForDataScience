import numpy as np
from PIL import Image


def ft_invert(img: np.ndarray) -> np.ndarray:
    '''ft_invert(img: np.array) -> np.array

Invert the image color by subtracting each pixel from 255
return the inverted image as a numpy array'''
    return 255 - img


def ft_red(img: np.ndarray) -> np.ndarray:
    '''ft_red(img: np.array) -> np.array

zero out the green and blue channels of the image
return the red image as a numpy array'''
    red, green, blue = Image.fromarray(img).split()
    zero_band = red.point(lambda p: 0)
    red_img = Image.merge('RGB', (red, zero_band, zero_band))
    return np.array(red_img)


def ft_green(img: np.ndarray) -> np.ndarray:
    '''ft_red(img: np.array) -> np.array

zero out the red and blue channels of the image
return the green image as a numpy array'''
    red, green, blue = Image.fromarray(img).split()
    zero_band = green.point(lambda p: 0)
    green_img = Image.merge('RGB', (zero_band, green, zero_band))
    return np.array(green_img)


def ft_blue(img: np.ndarray) -> np.ndarray:
    '''ft_red(img: np.array) -> np.array

zero out the red and green channels of the image
return the blue image as a numpy array'''
    red, green, blue = Image.fromarray(img).split()
    zero_band = blue.point(lambda p: 0)
    blue_img = Image.merge('RGB', (zero_band, zero_band, blue))
    return np.array(blue_img)


def ft_grey(img: np.ndarray) -> np.ndarray:
    '''ft_grey(img: np.array) -> np.array

Convert the image to greyscale
return the greyscale image as a numpy array'''
    grayscale = Image.fromarray(img).convert("L")
    return np.array(grayscale)
