import random

def swap(lst, i1, i2):
    """given list lst and indices i1, i2
        swaps the elements at indices i1 and i2"""
    tmp = lst[i1]
    lst[i1] = lst[i2]
    lst[i2] = tmp


def random_list(length, min, max):
    """returns list of length length with random integer elements in closed interval (min, max)"""
    lst = []
    for i in range(length):
        lst.append(random.randint(min, max))
    return lst


def split(list):
    """given list
    returns two lists that are the original list split in half, with the first half containing more elements if the length of the list is odd"""
    half = len(list) // 2
    return list[:half], list[half:]
