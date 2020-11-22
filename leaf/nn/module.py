class Module:

    def forward(self, *input):
        raise NotImplementedError

    def __call__(self, x):
        return self.forward(x)
