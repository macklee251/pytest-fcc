import sys
import math
import pytest
from faker import Faker
sys.path.append('./../')
from source.shapes import Circle

faker = Faker() 

class TestCircle:
    
    def test_circle_area(self):
        #arrange
        radio = faker.random_number()
        circle = Circle(radio)
        
        #act 
        result = circle.area()
        
        #assert
        assert result == math.pi * radio**2
        print(f'A area do circulo vale {result}')