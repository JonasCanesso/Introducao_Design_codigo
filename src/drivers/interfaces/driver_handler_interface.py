from abc import ABC, abstractmethod
from typing import List

class DriverHandlerInteface(ABC):

    @abstractmethod
    def standard_derivation(self, numbers: List[float]) -> float:
        pass