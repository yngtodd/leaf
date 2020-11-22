import numpy as np
import leaf.nn.functional as F

from .module import Module


class ReLU(Module):
    r"""ReLU activation function"""

    def __init__(self):
        super(ReLU, self).__init__()

    def forward(self, x):
        return F.relu(x)

