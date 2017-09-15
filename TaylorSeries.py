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


    class function:
        def __init__(function):
            self.f = function
            return

        def compute_function(function):
            n = function
            return [1,2,3,4]



    def __init__(func, n):
        self.f = self.function.compute_function(func)
        self.n = n_computed # takes the number
        return

    def factorial(self, n):
        if (n <= 1):
            return 1
        else:
            return n * self.factorial(n-1)

    def take_deriv(self):
        return

