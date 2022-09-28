from .foo import B


class A:
    def __init__(self):
        from .foo import B
        self.b = B()


def bar():
    pass
