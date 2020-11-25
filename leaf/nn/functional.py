import numpy as np


def relu(x):
    r"""ReLU activation function"""
    return np.maximum(0, x)


def softmax(x, dim=1):
    f"""Softmax activation function"""
    exp = np.exp(x, np.max(x, axis=dim, keepdims=True))
    probabilities = exp / np.sum(exp, axis=dim, keepdims=True)
    return probabilities
