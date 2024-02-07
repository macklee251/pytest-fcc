import sys
import pytest
from faker import Faker
sys.path.append('./../')
import source.my_functions as my_functions

faker = Faker()

def test_divide_any_to_numbers():
    #arrange 
    n1 = faker.random_number()
    n2 = 0
    
    #act 
    resultado = my_functions.divide(n1, n2)
    
    #assert
    assert resultado == "Não é possível dividir por zero."
    print(resultado)