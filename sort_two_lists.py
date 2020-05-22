import sys
from ast import literal_eval
from heapq import merge

def sort_two_lists(list1: list, list2: list) -> list:
    if not valid_list(list1):
        raise ValueError('Lists are expected to be sorted. {} is not sorted.'.format(list1))
    if not valid_list(list2):
        raise ValueError('Lists are expected to be sorted. {} is not sorted.'.format(list2))

    return list(merge(list1, list2))

def valid_list(l: list):
    return l == sorted(l)

def main(args):
    all_args = ''.join(args[1:])
    split_char = all_args.index(']') + 1
    list1 = literal_eval(all_args[:split_char])
    list2 = literal_eval(all_args[split_char:])
    print(sort_two_lists(list1, list2))

if __name__ == '__main__':
    main(sys.argv)
