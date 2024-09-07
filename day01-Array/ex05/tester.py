from PIL import Image
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

array = ft_load("../img/landscape.jpg")

Image.fromarray(ft_invert(array)).show()
Image.fromarray(ft_red(array)).show()
Image.fromarray(ft_green(array)).show()
Image.fromarray(ft_blue(array)).show()
Image.fromarray(ft_grey(array)).show()

print(ft_invert.__doc__)
