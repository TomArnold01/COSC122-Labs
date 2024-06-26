from quicksort import *


def read_data(filename):
    """ Returns a list of integers read from the file """
    with open(filename) as infile:
        values = [int(line.strip()) for line in infile]
    return values


def common_items(list_x, list_y):
    """ Takes two sorted lists as input (ie, both lists are in ascending order).
    Returns a list containing all the items in list_x that are also in list_y.
    Returns an empty list if there are none.

    The resulting list should be in order and only contain one instance of each
    item that appears in both lists, ie, common items should only be listed once.
    NOTE: You should use a method similar to the merge function in mergesort,
    that is, use a while loop and a couple of indices. Don't use any for loops!

    First write code for dealing with two lists that each contain only uniques values.
    When you have that running, update it so that it deals with lists that don't
    contain all unique values, see the commented doctests below

    NOTES:
    Your function will need to use only one while loop.
    Your function shouldn't use expressions like:
       - item in alist
       - for item in alist

    >>> common_items([0,1,2,3],[1,2,3,4])
    [1, 2, 3]
    >>> common_items([0,1,2,3],[0,1,2,3])
    [0, 1, 2, 3]
    >>> common_items([0,1,2,3],[5,6,7,8])
    []
    >>> common_items([],[5,6,7,8])
    []
    >>> common_items([1,2,3,4],[])
    []
    >>> common_items([],[])
    []
    >>> common_items([0,1,2,3],[0,0,2,4])
    [0, 2]
    >>> common_items([0,1,2,2,5,5,6,6,7],[0,0,2,4,5,5,5,7])
    [0, 2, 5, 7]
    """

    # ---start student section---
   # if list_x == str:
   #     list_1 = read_data(list_x)
   # if list_y == str:
   #     list_2 = read_data(list_y)
   # else:
   #     list_1 = list_x
   #     list_2 = list_y
   # print(list_1)
   # print(list_2)
    
    list_1 = read_data(list_x)
    list_2 = read_data(list_y)    
    
    return list(set(list_1).intersection(list_2))
    # ===end student section===


#if __name__ == "__main__":
#    doctest.testmod()

def test(list_x, list_y):
    
    
    list_of_shit = common_items(list_x, list_y)
    return len(list_of_shit)