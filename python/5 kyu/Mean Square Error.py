import numpy as np

def solution(array_a, array_b):
    return np.square(np.subtract(array_a, array_b)).mean()