import sys
import math
import pytest
from faker import Faker
sys.path.append('./../')
from source.shapes import Circle

faker = Faker() 

def test_circle_area():
    #arrange
    radio = faker.random_number()
    circle = Circle(radio)
    
    #act
    result = circle.area()
    
    #assert
    assert result == math.pi * radio**2
    print(f'A area do circulo vale {result}')