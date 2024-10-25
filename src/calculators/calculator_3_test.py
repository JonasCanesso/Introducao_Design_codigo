from typing import Dict, List
from pytest import raises
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInteface
from .calculator_3 import Calculator3

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body
    
class MockDriverHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 3

class MockDriverHandler:
    def variance(self, numbers: List[float]) -> float:
        return 10000000
    
def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(MockDriverHandlerError())
    
    with raises(Exception) as exinfo:
        calculator_3.calculate(mock_request)
    
    assert str(exinfo.value) == 'Falha no processo: Variância menor que multiplicação.'

def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(MockDriverHandler())
        
    response = calculator_3.calculate(mock_request)

    assert response == {'data': {'Calculator': 3, 'value': 10000000, 'Success': True}}
    
    