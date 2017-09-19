class trigonometric:
        def __init__(self, trigfunc):
            self.f = trigfunc
            print(self.f)
            self.dictionary = ["sin(x)", "cos(x)", "tan(x)", "csc(x)", "sec(x)",
                               "cot(x)", "arcsin(x)", "arccos(x)", "arctan(x)",
                               "arccsc(x)", "arcsec(x)", "arccot(x)"]
            self.pos = 0
            self.identity = self.identify()
            return

        def identify(self):
            count = 0
            for s in self.dictionary:
                if self.f == s:
                    self.pos = count
                    identity = self.dictionary[self.pos]
                    return identity
                count += 1
                
        def return_dictionary(self):
            return self.dictionary

        def perform_derivative(self):
            return

n = trigonometric("m")
print(n.identity)
