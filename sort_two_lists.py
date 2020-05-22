import sys
from ast import literal_eval
from heapq import merge

def sort_two_lists(list1: list, list2: list) -> list:
    # The progam specifies that the input will be sorted lists
    # (including the empty list). Because we will give incorrect
    # output if the input lists are not sorted, here's some basic error checking
    if not valid_list(list1):
        raise ValueError('Lists are expected to be sorted. {} is not sorted.'.format(list1))
    if not valid_list(list2):
        raise ValueError('Lists are expected to be sorted. {} is not sorted.'.format(list2))

    return list(merge(list1, list2)) # the core functionality is a one-liner

def valid_list(l: list) -> bool:
    # I broke this out into a separate function so we can add more
    # validity requirements later if need be. We're finding out if
    # the lists are sorted and if they're either empty or contain only digits.
    if l != sorted(l):
        return False
    for i in l:
        if not (isinstance(i, int) or isinstance(i, float)):
            return False
    return True

def main(args):
    # The most challenging part of this assignment is allowing the program to parse
    # a list literal from bash as input. I settled on basic string slicing from sys.argv,
    # which is sort of quick and dirty, but it functions perfectly well and allows
    # for pretty simple failure detection.

    all_args = ''.join(args[1:]) # get input as a single list
    try:
        split_char = all_args.index(']') + 1
    except ValueError:
        raise ValueError('This program takes two lists as input; no input lists were found.')
    list1 = literal_eval(all_args[:split_char]) # I hate using literal_eval, for the record
    try:
        list2 = literal_eval(all_args[split_char:])
    except SyntaxError:
        raise ValueError('This program takes two lists as input; only one list was found.')
    print(sort_two_lists(list1, list2))

if __name__ == '__main__':
    main(sys.argv)
