"""
Binary search tree implementation
http://algoviz.org/OpenDSA/dev/OpenDSA/build/BST.html

I K Stead
13/08/2012
"""

class Node(object):
    """
    Represent a node in the binary search tree
    """
    def __init__(self, data):
        self.data = data
        self.l_child = None
        self.r_child = None

    def insert(self, data):
        """
        Recursively insert a node into this node's subtree
        """
        if data < self.data:
            if not self.l_child:
                self.l_child = Node(data)
            else:
                self.l_child.insert(data)
        else:
            if not self.r_child:
                self.r_child = Node(data)
            else:
                self.r_child.insert(data)

    def inorder(self, fn=None):
        """
        Inorder traversal, performing some function on each node. 
        
        Due to the BST property, the resulting enumeration
        will be in sorted order, from lowest to highest.
        """
        # Visit left child and its subtree
        if self.l_child:
            self.l_child.inorder(fn)
        # Call the supplied function on the node's data
        if fn:
            fn(self.data)
        # Visit the right child and its subtree
        if self.r_child:
            self.r_child.inorder(fn)
        return

    def search(self, key):
        """
        Recursively search node and subtree for key value
        """
        if self.data == key:
            return self
        if key < self.data and self.l_child:
            return self.l_child.search(key)
        if key >= self.data and self.r_child:
            return self.r_child.search(key)
        
        return False

def binary_tree(data_list):
    """
    Create a binary tree of nodes from iterable containing ordinal data
    """
    root = Node(data_list[0])
    for el in data_list[1:]:
        root.insert(el)
    return root

def __test__():
    data = [37, 24, 42, 7, 2, 40, 42, 32, 120]
    tree = binary_tree(data)
    x =  tree.search(42)
    print x.data, x.l_child, x.r_child
