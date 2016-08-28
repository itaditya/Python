#!/usr/bin//env python2.7
class rootFinder(object):
    """docstring for rootFinder"""

    def __init__(self, fn):
        self.array = []
        self.root = 0
        self.tolerance = 0.000001
        self.recurrence_fn = fn

    def expression_generator(self):
        expression = ""
        for i in range(len(self.array)):
            expression += str(i)[::-1] + "^x" + \
                str(self.array[i])[::-1] + " + "
        expression = expression[::-1]
        print("The Expression you wrote is :")
        print(("_" * 15) + "\n")
        print expression[3:len(expression) - 3]
        print("_" * 15)

    def fn_evaluate(self, x):
        result = 0
        for i in range(len(self.array)):
            result += self.array[i] * (x**i)
        return result

    def initial_domain(self):
        i = 0
        while (self.fn_evaluate(i) * self.fn_evaluate((i + 1)) >= 0):
            i += 1
        return (i, (i + 1))

    def root_finder(self, a, b):
        f_a = self.fn_evaluate(a)
        f_b = self.fn_evaluate(b)

        # x = float((a * f_b - b * f_a) / (f_b - f_a))
        x = float(self.recurrence_fn(a, b, f_a, f_b))

        f_x = self.fn_evaluate(x)
        if (abs(f_x) - self.tolerance > 0):
            if (f_x * f_a < 0):
                return self.root_finder(a, x)
            else:
                return self.root_finder(x, b)
        else:
            self.root = x

    def input_params(self):
        tolerance = float(raw_input("Enter the correct decimal place\n"))
        coeff = map(float, raw_input(
            "\nEnter the coefficients of x from higher to lower degree order\n").split())
        coeff = coeff[::-1]
        self.array = (coeff)
        self.tolerance = tolerance
        # Now the list has the terms with index same as the power of x .

    def show_root(self):
        print("The root is : " + str(self.root))

# finder = rootFinder()
# finder.input_params()
# finder.expression_generator()
# a, b = finder.initial_domain()
# finder.root_finder(a, b)
# finder.show_root()
