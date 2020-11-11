import numpy as np

def calculate(list):
    if len(list) < 9:
        return "List must contain nine numbers."
    arr = np.array(list).reshape(3,3)
    print(arr)
    calculations = dict()

    return calculations