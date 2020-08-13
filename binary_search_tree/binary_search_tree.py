"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if there is no root value
        if self is None:
            # create a new node
            self = BSTNode(value)
        # check if value is smaller than the targeted node
        if value < self.value:
            # if there already is a value to the left
            if self.left is not None:
                self.left.insert(value)
            # if there isn't a value to the left
            else:
                # create a new node with this value
                self.left = BSTNode(value)
        # else, the value is larger than the targeted node
        else:
            # if there already is a value to the right
            if self.right is not None:
                self.right.insert(value)
            # if there isn't a value to the right
            else:
                # create a new node with this value
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # create a variable to hold the current node
        current_node = self

        while current_node is not None:
            # check if the current node matches the target
            if target == current_node.value:
                # if so, yes the tree contains this value
                return True
            # check if the target is smaller than the current node
            elif target <= current_node.value:
                # if so, set the current node to the smaller value (on the left)
                current_node = current_node.left
            # else, the target is larger than the current node
            else:
                # set the current node to the larger value (on the right)
                current_node = current_node.right
        
        # if the value wasn't found, the value isn't in the tree
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # create a variable to hold the current node/the furthest right we've traversed
        current_node = self
        # while there is a node to the right
        while current_node.right is not None:
            # set the current to the larger number to the right
            current_node = current_node.right
        return current_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function on the root node
        fn(self.value)
        # check if there is a left child
        if self.left:
            # begin the process on the left child
            self.left.for_each(fn)
        # check if there is a right child
        if self.right:
            # begin the process on the right child
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  

# renamed in_order_dft to in_order_print, still getting an error though
