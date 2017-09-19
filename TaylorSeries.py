import math

"""This class will deal with taylor series of given functions."""

"""let y = f(x) 
   for a given function f, the taylor series of that function will be equal to:
   Sum (n=0 --> n=k), where k{I+}, (fDeriv(I)(0)/I!)x^I
   This can be broken up into n parts:
   I factorial: factorial(I)
   Derivative of f(x) at point 0 can be approximated using newtons step method
        Subsequently the df(0) can be found by plugging in 0 at the derivative
   Finally, these components will be computed, and summed accordingly
"""

class Taylor_Series:




    def __init__(func, n):
        self.f = self.function(func)
        self.n = n_computed # takes the number
        return

    def factorial(self, n):
        if (n <= 1):
            return 1
        else:
            return n * self.factorial(n-1)

    def take_deriv(self, x, y):
        #take the tangent line at a given function f at point x,y
        slope = (y-(y+0.00000001))/(x-(x+0.00000001))
        return slope

