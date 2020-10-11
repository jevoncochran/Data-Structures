from queue import Queue
from stack import Stack

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
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else: 
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
        # while current.right is not None:
        #     current = current.right
        # return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
           self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = [node]

        while q:
            n = q.pop(0)
            print(n.value)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # print(node.value)
        # if node.left:
        #     self.dft_print(node.value)
        # if node.right:
        #     self.dft_print(node.value)
        stack = Stack()

        stack.push(node)
        while len(stack) > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)
        
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.left.pre_order_dft(node.left)
        if node.right:
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.left.post_order_dft(node.left)
        if node.right:
            node.right.post_order_dft(node.right)
        print(node.value)
