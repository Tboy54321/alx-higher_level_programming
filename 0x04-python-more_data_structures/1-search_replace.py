#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    count = 0
    for n in new_list:
        count += 1
        if n == search:
            new_list[count] = replace
    return (new_list)
