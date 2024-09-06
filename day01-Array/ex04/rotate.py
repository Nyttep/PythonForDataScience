import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    img_arr: np.ndarray = ft_load("../img/animal.jpeg")
    if img_arr is None:
        exit(1)

    zoomed: Image.Image = Image.fromarray(img_arr).crop((200, 200, 600, 600))

    grayscale: Image.Image = zoomed.convert(mode="L")

    nb_channels = len(grayscale.getbands())
    shape = f"({grayscale.height}, {grayscale.width}, {nb_channels})"
    print(f"The shape of image is: {shape} or {grayscale.size}")
    print(np.asarray(grayscale))

    transposed: np.ndarray = np.array(grayscale).copy()
    grayscale_arr = np.asarray(grayscale)
    for line in range(grayscale.height):
        for col in range(grayscale.width):
            transposed[line, col] = grayscale_arr[col, line]
    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)
    plt.imshow(transposed, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
