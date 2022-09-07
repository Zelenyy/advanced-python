"""
Who lives in a pineapple under the sea?
"""


class Rectangular:
    """
    Bob Gubko kvadratni shtani
    """
    def __init__(self, height: int, width : int):
        self._check_values(height, width)
        self.height, self.width = height, width

    @staticmethod
    def _check_values(*values):
        for value in values:
            if not isinstance(value, int):
                raise TypeError
            if value < 0:
                raise ValueError

    @property
    def area(self):
        return self.height*self.width

    def resize(self, height: int, width: int):
        self._check_values(height, width)
        self.height, self.width = height, width