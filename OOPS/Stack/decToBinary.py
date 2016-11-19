#!/usr/bin/env python3
from stack import Stack


def rec_conv(binary, dec_no):
    next = dec_no // 2
    binary.push(dec_no % 2)
    if (next != 0):
        rec_conv(binary, next)


def decToBinary(dec_no):
    s = Stack()
    rec_conv(s, dec_no)
    # return s
    return "".join(map(str, s.items[::-1]))

dec_no = int(input("Enter A Decimal Number : "))
print(str(dec_no) + " in Binary is " + decToBinary(dec_no))
