import numpy as np

def ft_invert(img: np.ndarray) -> np.ndarray:
    '''ft_invert(img: np.array) -> np.array

Invert the image color by subtracting each pixel from 255

return the inverted image as a numpy array'''
    return 255 - img

def ft_red(img: np.ndarray) -> np.ndarray:
    '''ft_red(img: np.array) -> np.array

Return the red channel of the image

return the red image as a numpy array'''
    return img[:, :, 0]