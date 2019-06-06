import math

class CoolCalc(object):
    """A simple calculator class"""
    def __init__(self):
        pass

    def add_a_b(self, a, b):
        """Take two numbers and return the sum."""
        return a + b

    def multiply_a_b(self, a, b):
        """Take two numbers and return the product."""
        return a * b

    def power_a_b(self, a, b):
        """Take two numbers and raise a to the power of b"""
        return a ** b
    
    def divide_a_b(self, a, b):
        """Take two numbers and divide a by b"""
        return a / b

    def cosine_a(self, a):
        """Take cosine of a radians"""
        return math.cos(a)

