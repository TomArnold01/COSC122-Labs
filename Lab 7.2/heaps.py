""" A module dedicated to the 2-heap """
import doctest
import os


#--------------------------------------------------------------------------
def load_file(file_name):
    """ Returns a list of numbers from the file.
        The file should contain one integer per line.
    """
    with open(file_name) as infile:
        lines = infile.read().splitlines()
    nums = [int(line) for line in lines]
    return nums


#-------------------------------------------------
#-------------------------------------------------
class Heap(object):

    """An abstract interface for a Heap."""

    def __init__(self):
        # Create a list to store heap items.
        # First item is simply a spacer
        # Heap contents will start from index 1
        self._items = [None]

    def insert(self, item):
        # don't implement here
        # this is just a place holder
        pass

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        """Returns the actual length of the heap,
        ie, how many items are in the heap
        Remember that item at index 0 is not part of the heap."""
        return len(self._items) - 1

    def __repr__(self):
        """Returns the _items list for the heap
        Note, there will be a None at index 0
        and this is just a place holder.
        The root value is at index 1"""
        return repr(self._items)


#-------------------------------------------------
#-------------------------------------------------
class MinHeap(Heap):
    """Implementation of a min-heap."""

    # note: inherits __init__ from Heap

    #---------------------------------------------
    def insert(self, item):
        """Inserts a given item into the heap.

        >>> h = MinHeap()
        >>> h.insert(3)
        >>> h._items
        [None, 3]
        >>> h.insert(7)
        >>> h._items
        [None, 3, 7]
        >>> h.insert(5)
        >>> h._items
        [None, 3, 7, 5]
        >>> h.insert(2)
        >>> h._items
        [None, 2, 3, 5, 7]
        >>> h.insert(4)
        >>> h._items
        [None, 2, 3, 5, 7, 4]
        """
        # ---start student section---
        self._items.append(item)
        index = self.__len__()
        self._sift_up(index)
        # ===end student section===

    #-------------------------------------------------
    def _sift_up(self, index):
        """
        Moves the item at the given index up through the heap until it finds
        the correct place for it. That is, the item is moved up through the heap
        while it is smaller than its parent.
        """
        parent = (index) // 2
        # While we haven't reached the top of the heap, and its parent is
        # smaller than the item
        if index > 1 and self._items[index] < self._items[parent]:
            # Swap the item and its parent
            self._items[index], self._items[parent] = self._items[parent], self._items[index]
            # Carry on sifting up from the parent index
            self._sift_up(parent)
        # else no more sifting needed as didn't swap.

    #-------------------------------------------------

    def peek_min(self):
        """
        Returns the smallest item in the heap.

        >>> h = MinHeap()
        >>> h.insert(5)
        >>> h.validate()
        True
        >>> h.peek_min()
        5
        >>> h.insert(3)
        >>> h.peek_min()
        3
        >>> h.insert(7)
        >>> h.peek_min()
        3
        >>> h.insert(1)
        >>> h.peek_min()
        1
        """
        return self._items[1]

    #-------------------------------------------------
    def pop_min(self):
        """
        Removes the smallest item in the heap and returns it. Returns None if
        there are no items in the heap. Can be thought of as Popping the min
        item off the heap.

        >>> h = MinHeap()
        >>> h.insert(5)
        >>> h.pop_min()
        5
        >>> len(h)
        0
        >>> h.insert(3)
        >>> h.insert(7)
        >>> h.pop_min()
        3
        >>> h.pop_min()
        7
        >>> h.pop_min() is None
        True
        >>> len(h)
        0
        >>> tmp = list(map(h.insert, (3, 7, 5, 2, 4)))
        >>> h.pop_min()
        2
        >>> h._items[1]
        3
        >>> h._items[2]
        4
        >>> h.pop_min()
        3
        """
        # ---start student section---
        
        # add cause for if the array is empty
        
        if self._items.__len__() == 1:
            return None
        else:
            smallest = self._items[1] 
            self._items[1] = self._items[-1]
            del self._items[-1]
        index = 1
        self._sift_down(index)
        return smallest
        # ===end student section===

    #-------------------------------------------------
    def _sift_down(self, index):
        """
        Moves an item at the given index down through the heap until it finds
        the correct place for it. That is, when the item is moved up through the
        heap while it is larger than either of its children.
        """
        # While the item at 'index' has at least one child...
        if (index * 2) <= len(self):
            left = 2 * index
            right = left + 1
            smallest = left
            if self._items[index] > self._items[smallest]:
                self._items[smallest], self._items[index] = self._items[index], self._items[smallest]
                self._sift_down(smallest)
            # else nothing more to do as didn't swap

    #-------------------------------------------------
    def validate(self):
        """
        Validates the heap. Returns True if the heap is a valid min-heap, and
        False otherwise.

        >>> h = MinHeap()
        >>> h._items = [None, 1, 3, 5]
        >>> h.validate()
        True
        >>> h._items = [None, 1, 3, 5, 8, 9, 6, 7, 11]
        >>> h.validate()
        True
        >>> h._items = [None, 2, 3, 1, 7]
        >>> h.validate()
        False
        >>> h._items = [None, 5, 7, 2]
        >>> h.validate()
        False
        """

        # ---start student section---
        if self._items.__len__() <= 2:
            return  True
        else:
            
            if self._items[1] <= self._items[2] and self._items[1] <= self._items[3]:
                return True
            else:
                return False
        # ===end student section===


#if __name__ == '__main__':
    #os.environ['TERM'] = 'linux'  # Suppress ^[[?1034h
    #doctest.testmod()


h = MinHeap()
h.insert(78)
print(h._items)
h.insert(74)
print(h._items)
h.insert(50)
print(h._items)
h.insert(60)
print(h._items)
h.insert(82)
print(h._items)
h.insert(34)
print(h._items)
h.insert(16)
print(h._items)
print(h.validate())   # this currently returns False needs to turn True
print("*******************************")
h = MinHeap()
h.insert(54)
print(h._items)
h.insert(82)
print(h._items)
h.insert(38)
print(h._items)
h.insert(46)
print(h._items)
h.insert(20)
print(h._items)
print(h.validate())