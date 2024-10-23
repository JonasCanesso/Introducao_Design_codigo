import numpy
from typing import List

class NumpyHandler:
    def __init__(self) -> None:
        self.np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        return self.np.std(numbers)