#!/usr/bin//env python3
print('Hello User\nI find the root of functions using Bissection Method \n ')


def expression_generator(coeff):
    expression = ""
    for i in range(len(coeff)):
        expression += str(i)[::-1] + "^x" + str(coeff[i])[::-1] + " + "
    expression = expression[::-1]
    print("The Expression you wrote is :")
    print(("_" * 15) + "\n")
    print expression[3:len(expression) - 3]
    print("_" * 15)


def fn_evaluate(coeff, x):
    result = 0
    for i in range(len(coeff)):
        result += coeff[i] * (x**i)
    return result


def initial_domain(coeff):
    i = 0
    while (fn_evaluate(coeff, i) * fn_evaluate(coeff, (i + 1)) >= 0):
        i += 1
    return (i, (i + 1))


def root_finder(coeff, a, b, tolerance):
    f_a = fn_evaluate(coeff, a)
    f_b = fn_evaluate(coeff, b)

    x = float((a * f_b - b * f_a)) / (f_b - f_a)

    f_x = fn_evaluate(coeff, x)
    if (abs(f_x) - tolerance > 0):
        if (f_x > 0):
            return root_finder(coeff, a, x, tolerance)
        else:
            return root_finder(coeff, x, b, tolerance)
    else:
        return x


def main():
    i = 0
    no_of_terms = int(input("Enter the highest power\n")) + 1
    tolerance = float(input("Enter the correct decimal place\n"))
    coeff = []
    print("\nEnter the coefficients of x from higher to lower degree order")
    while (i < no_of_terms):
        coeff.append(float(input()))
        i += 1
    coeff = coeff[::-1]
    # Now the list has the terms with index same as the power of x .
    expression_generator(coeff)
    a, b = initial_domain(coeff)
    root = root_finder(coeff, a, b, tolerance)
    print("The root is : " + str(root))

main()
