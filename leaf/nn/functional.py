import numpy as np


def relu(x):
    r"""ReLU activation function"""
    return np.maximum(0, x)
