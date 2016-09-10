from stack import Stack


def isOperation(operator):
    if(operator == '^' or operator == '*' or operator == '/' or operator == '+' or operator == '-'):
        return True
    else:
        return False
    # print("Not a valid operator")


def postfixConv():
    s = Stack()
    expression = list(raw_input())
    i = 0
    a = 0
    b = 0
    operators = {
        "+": (lambda x, y: x + y)(a, b),
        "-": (lambda x, y: x - y)(a, b),
        "*": (lambda x, y: x * y)(a, b),
        # "/": (lambda x, y: x / y)(a, b),
        "^": (lambda x, y: x ^ y)(a, b)
    }
    l = len(expression)
    print operators.get(expression[i])(2, 3)
    # while(i < l):
    #     if(isOperation(expression[i])):
    #         # means we get operations
    #         y = s.pop()
    #         x = s.pop()
    #         # res = operation(x, y, expression[i])
    #         res = operators.get(expression[i])
    #         s.push(res)
    #     else:
    #         # means we get operands
    #         s.push(expression[i])
    #     i += 1
    # print s.peek()

postfixConv()

# a + b + c
