from PIL import Image
import numpy as np


def ft_load(path: str)-> np.array:
    '''ft_load(path: str)-> np.array
    
Load an image from the path, 
print its format and its pixel content in RGB format
return the image as a numpy array
If the image can't be loaded return None and prints the error'''
    try:
        img = Image.open(path)
    except IOError:
        if path == None:
            print("Error: No path provided")
        elif path == "":
            print("Error: Empty path provided")
        else:
            print("Error: Can't open the file")
    else:
        with img:
            img_arr = np.array(img)
            # this is awful but eh i do what the subject says
            print(f"The shape of image is: {img_arr.shape}")
            return img_arr
