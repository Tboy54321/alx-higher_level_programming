#!/usr/bin/python3
def search_replace(my_list, search, replace):
    count = 0
    for n in my_list:
        count += 1
        if n == search:
            my_list[count] = replace
    return my_list
