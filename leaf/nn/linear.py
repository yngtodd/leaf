import numpy as np


class Linear:
    r"""Fully connected layer

    Args:
        n_inputs: input dimension
        n_neurons: number of neurons in the layer
    """

    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def __call__(self, x):
        return self.forward(x)

    def forward(self, x):
        return np.dot(x, self.weights) + self.biases
