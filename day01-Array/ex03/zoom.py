from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    img_arr = ft_load("landscape.jpg")
    if img_arr is None:
        exit(1)
    print(img_arr)
    zoomed = Image.fromarray(img_arr).crop((200, 200, 600, 600))
    grayscale = zoomed.convert(mode="L")
    nb_channels = len(grayscale.getbands())
    shape = f"({grayscale.height}, {grayscale.width}, {nb_channels})"
    print(f"New shape after slicing: {shape} or {grayscale.size}")
    print(np.asarray(grayscale))
    plt.imshow(grayscale, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
