
class PyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]

    def __iter__(self):
        for c in self.items:
            yield c
