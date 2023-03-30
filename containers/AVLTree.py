'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in
the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a
        balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        ret = True
        if node is None:
            pass
        elif node.right is None and node.left:
            if node.left.left or node.left.right:
                ret = False
        elif node.left is None and node.right:
            if node.right.left or node.right.right:
                ret = False
        elif AVLTree._balance_factor(node) in [-1, 0, 1]:
            if node.left is not None:
                ret &= AVLTree._is_avl_satisfied(node.left)
            if node.right is not None:
                ret &= AVLTree._is_avl_satisfied(node.right)
        else:
            ret = False
        return ret

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        old_root_val = node.value
        new_root = node.right
        node.value = node.right.value
        old_root_right = node.right.left
        old_root_left = node.left
        node.value = new_root.value
        node.right = new_root.right
        node.left = Node(old_root_val, old_root_left, old_root_right)
        return node

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        old_root_val = node.value
        new_root = node.left
        node.value = node.left.value
        old_root_right = node.right
        old_root_left = node.left.right
        node.value = new_root.value
        node.left = new_root.left
        node.right = Node(old_root_val, old_root_left, old_root_right)
        return node

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to
        insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert
        function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if self.root is None:
            self.root = Node(value)
        else:
            BST._insert(self.root, value)
        if AVLTree._is_avl_satisfied(self.root) is False:
            AVLTree._correct(self.root, value)
        return

    @staticmethod
    def _correct(node, value):
        if node is None:
            return
        if AVLTree._is_avl_satisfied(node) is False:
            if AVLTree._balance_factor(node) in [-2, 2]:
                AVLTree._rebalance(node)
            if value < node.value:
                AVLTree._correct(node.left, value)
            if value > node.value:
                AVLTree._correct(node.right, value)
        else:
            return

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                AVLTree._right_rotate(node.right)
                AVLTree._left_rotate(node)
            else:
                node = AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                AVLTree._left_rotate(node.left)
                AVLTree._right_rotate(node)
            else:
                node = AVLTree._right_rotate(node)
