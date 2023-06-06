#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_no = number % -(10)
        print(-(last_no), end="")
    else:
        last_no = number % 10
        print(last_no, end="")
    return abs(last_no)
