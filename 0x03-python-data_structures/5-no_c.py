#!/usr/bin/python3
def no_c(my_string):
    act_string = ""
    for i in my_string:
        if i != "c" and i != "C":
            act_string += i
    return (act_string)
