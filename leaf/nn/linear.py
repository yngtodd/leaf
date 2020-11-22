import numpy as np

from .module import Module


class Linear(Module):
    r"""Fully connected layer

    Args:
        n_inputs: input dimension
        n_neurons: number of neurons in the layer
    """

    def __init__(self, n_inputs, n_neurons):
        super(Module, self).__init__()
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, x):
        return np.dot(x, self.weights) + self.biases
