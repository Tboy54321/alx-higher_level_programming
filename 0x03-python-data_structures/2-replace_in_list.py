#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
<<<<<<< HEAD
    if idx < 0 or idx > len(my_list):
        return ("None")
    else:
        my_list[idx] = element
        return my_list
=======
    my_list[idx] = element
    return my_list
>>>>>>> 794ae976187db9525b3cc3afc0377ac589d2afae
