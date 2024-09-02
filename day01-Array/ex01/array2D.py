import numpy as np


def slice_me(family: list[list], start: int, end: int) -> list:
    '''slice_me(family: list[list], start: int, end: int) -> list

Return a slice of the input list from start to end
If the lists are not the same size return an empty list
If the args are wrong types return an empty list'''
    try:
        lenghts = [len(i) for i in family]
        if lenghts.count(lenghts[0]) != len(lenghts):
            return []

        arr = np.array(family)
        print(f"My shape is : {arr.shape}")
        arr = arr[start:end]
        print(f"My new shape is : {arr.shape}")
        return arr.tolist()
    except TypeError:
        return []
