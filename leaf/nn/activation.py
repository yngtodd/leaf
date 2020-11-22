import numpy as np
import leaf.nn.functional as F

from .module import Module


class ReLU(Module):
    r"""ReLU activation function"""

    def __init__(self):
        super(ReLU, self).__init__()

    def forward(self, x):
        return F.relu(x)


def Softmax(Module):
    r"""Softmax activation function"""

    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x, dim=1):
        return F.softmax(x)

