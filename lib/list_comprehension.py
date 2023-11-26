#!/usr/bin/env python3

def return_evens(num_list):
    # !using for loop
    # evenNumbers = list()

    # for item in range(10):
    #     if item % 2 == 0:
    #         evenNumbers.append(item)
    # return evenNumbers

    # using list comperehension
    evenNumbersLc = [item for item in num_list if item % 2 == 0]

    return evenNumbersLc


# print(return_evens([0, 1, 3, 5, 7, 8, 9]))


def make_exclamation(sentence_list):
    # !using for loop
    # sentenceStrings = []

    # for item in sentence_list:
    #     sentenceStrings.append(f"{item}!")

    # return sentenceStrings

    # !using list comperehension
    sentenceStringsLc = [f"{item}!" for item in sentence_list]

    return sentenceStringsLc


# print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
