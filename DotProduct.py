import math

class vector_operands:

    """ |v||u|cos(a) = a1b1 + a2b2 ..."""
    def __init__(self, vector_1, vector_2):
        self.v1 = vector_1
        self.v2 = vector_2
        return

    def dot_product(self):
        mag = self.magnitude()
        RHS = (self.sum_comp())/(mag[0]*mag[1])
        theta = self.arccos(RHS)
        return theta

    def sum_comp(self):
        sum = 0
        for i in self.v1:
            for j in self.v2:
                sum += i*j
        return sum

    def magnitude(self):
        mag_1 = 0
        mag_2 = 0
        for i in self.v1:
            mag_1 += i**2
        mag_1 = mag_1**0.5

        for j in self.v2:
            mag_2 += j**2
        mag_2 = mag_2**0.5
        magnitudes = [mag_1, mag_2] # where magnitude[0] is v1, magnitude[1] is v2
        return magnitudes

    def arccos(self, x):
        theta = 1 - (self.arccos_term(2,x)) + (self.arccos_term(4,x)) - (self.arccos_term(6,x)) + (self.arccos_term(8,x)) - (self.arccos_term(10,x))
        return theta

    def factorial(self, n):
        if (n <= 1):
            return 1
        else:
            return n * self.factorial(n-1)

    def arccos_term(self, degree, x):
        x = x**2
        term = x/(self.factorial(degree))
        return term




