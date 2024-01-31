#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        value = max(a_dictionary.values())
        return[j for j, val in a_dictionary.items() if val == value][0]
