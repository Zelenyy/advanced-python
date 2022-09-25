
class A:
    def __init__(self):
        from files.general_overview.loading.foo import B
        self.b = B()

def bar():
    pass