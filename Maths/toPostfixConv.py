from stack import Stack


def prec(operator):
    if(operator == '^'):
        return 3
    elif(operator == '*' or operator == '/'):
        return 2
    elif(operator == '+' or operator == '-'):
        return 1
    else:
        return -1
    # print("Not a valid operator")


def postfixConv():
    s = Stack()
    expression = list(raw_input())
    i = 0
    postfixExp = ""
    l = len(expression)
    while(i < l):
        if(prec(expression[i]) != -1):
            # means we get operations
            if(prec(s.peek()) < prec(expression[i])):
                # simple situation
                s.push(expression[i])
            else:
                postfixExp += s.pop()
                s.push(expression[i])
        else:
            # means we get operands
            postfixExp += expression[i]
        i += 1
    while(prec(s.peek()) != -1):
        postfixExp += s.pop()
    print postfixExp

postfixConv()

# a + b + c
