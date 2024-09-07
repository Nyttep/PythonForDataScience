from load_image import ft_load
import numpy as np
from PIL import Image
from pimp_image import ft_invert

array = ft_load("../img/landscape.jpg")

Image.fromarray(ft_invert(array)).show()

