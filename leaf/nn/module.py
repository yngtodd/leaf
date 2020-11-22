class Module:
    r"""Base class for all neural net modules"""

    def forward(self, *input):
        raise NotImplementedError

    def __call__(self, x):
        return self.forward(x)
