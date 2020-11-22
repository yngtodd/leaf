import numpy as np


def relu(x):
    r"""ReLU activation function"""
    return np.maximum(0, x)


def softmax(x):
    f"""Softmax activation function"""
    exp = np.exp(x)
    return exp / np.sum(exp)
