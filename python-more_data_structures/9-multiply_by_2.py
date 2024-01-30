#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    copy = a_dictionary.copy()
    for j in copy:
        copy[j] *= 2
    return copy
