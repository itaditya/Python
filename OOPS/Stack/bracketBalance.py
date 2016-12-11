#!/usr/bin/env python3

from stack import Stack


def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            # that is ) bracket
            if (s.is_empty()):
                # checked whether ) is left alone
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False

print(par_checker("(((((())))"))
print(par_checker("(())"))
print(par_checker("((())"))
