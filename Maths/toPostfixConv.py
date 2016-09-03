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
    expression = (raw_input()).split()
    i = 0
    while(i < len(expression)):
        if(prec(expression[i]) != -1):
            # means we get operations
            if(prec(s.peek()) < prec(expression[i])):
                # simple situation
                s.push(expression[i])
            else:
                print(s.pop()),
                s.push(expression[i])
        else:
            # means we get operands
            print(expression[i]),
        i += 1
    while(prec(s.peek()) != -1):
        print(s.pop()),

postfixConv()

# a + b + c
