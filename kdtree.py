"""
K-dimensional search tree implementation
http://algoviz.org/OpenDSA/dev/OpenDSA/build/KDtree.html

I K Stead, 14/08/2012
"""

# discriminator defined as i % k at level i

class Node(object):
    """
    Represents a node in the k-d tree
    """
    def __init__(self, data, level=0):
        self.data = data
        self.l_child = None
        self.r_child = None
        self.level = level

    def insert(self, data):
        """
        Recursively insert a node into this node's subtree.

        Data comparison cycles through data item index 0 to k as tree
        increases depth.
        """
        d = self.level % len(data) # Discriminator

        if data[d] < self.data[d]:
            if not self.l_child:
                self.l_child = Node(data, self.level + 1)
            else:
                self.l_child.insert(data)
        else:
            if not self.r_child:
                self.r_child = Node(data, self.level + 1)
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

def kdtree(data_list):
    """
    Create and return a new k-d tree from supplied list of ordinal data
    """
    root = Node(data_list[0])
    for el in data_list[1:]:
        root.insert(el)
    return root

def __test__():
    point_list = [(40, 45), (15, 70), (70, 10), (69, 50), (66, 85), (85, 90)]
    kd = kdtree(point_list)
    print kd.data, kd.l_child.data, kd.r_child
