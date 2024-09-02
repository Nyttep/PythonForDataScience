import numpy as np


def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    '''give_bmi(height: list[int | float], weight: list[int | float])
-> list[int | float]

Return a list of all the ibm computed with the input lists
If the lists are not the same size
the length of the returned list is equal to the lenght of the smaller list
If the args are wrong types return an empty list'''
    try:
        #duplicate of try except just to show i know how to do it properly
        if not all(isinstance(i, (int, float)) for i in height + weight):
            return []
        h = np.array(height)
        w = np.array(weight)
        return (w[:h.size] / np.square(h[:w.size])).tolist()
    except TypeError:
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''apply_limit(bmi: list[int | float], limit: int) -> list[bool]

return a list of boolean values where True means
the bmi is greater than the limit
If the args are wrong types return an empty list'''
    try:
        #duplicate of try except just to show i know how to do it properly
        if not all(isinstance(i, (int, float)) for i in bmi):
            return []
        bmi_a = np.array(bmi)
        return (bmi_a > limit).tolist()
    except TypeError:
        return []
