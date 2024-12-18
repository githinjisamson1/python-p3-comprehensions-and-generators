#!/usr/bin/env python3

def return_evens(num_list):
    return [item for item in num_list if item % 2 == 0]


def make_exclamation(sentence_list):
    return [f"{item}!" for item in sentence_list]


print(return_evens([0, 1, 2, 3, 4, 5]))
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
