"""
Binary search trees in Python

I K Stead, 13/08/2012
"""

class BST(object):
    """
    Represents a binary search tree.
    http://en.wikipedia.org/wiki/Binary_search_tree
    """
    def __init__(self, value_list):
        """
        Recursively construct a binary search tree.
        """
        if value_list:
            sorted_values = sorted(value_list)
            mid = len(sorted_values) // 2

            self.value = sorted_values[mid]
            self.left_child = BST(sorted_values[:mid-1])
            self.right_child = BST(sorted_values[mid+1:])
        else:
            self.value = None
            self.right_child = None
            self.left_child = None

    
