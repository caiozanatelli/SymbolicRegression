from utils import Utils
import numpy as np
import random

class Chromossome:
    """ A Chromossome representation as a binary tree """

    __left_child  = None
    __right_child = None
    __symbol      = None

    def __init__(self, symbol, left=None, right=None):
        self.__left_child  = left
        self.__right_child = right
        self.__symbol = symbol

    def __str__(self):
        return str(self.__symbol) if self is not None else ' '

    def get_left_child(self):
        return self.__left_child

    def set_left_child(self, left):
        self.__left_child = left

    def get_right_child(self):
        return self.__right_child

    def set_right_child(self, right):
        self.__right_child = right

    def get_symbol(self):
        return self.__symbol

    def set_symbol(self, symbol):
        self.__symbol = symbol

    def get_chromossome_size(self):
        """
        Calculate the size of a chromossome recursively.

        Returns:
            [int] -- the size of the chromossome.
        """
        if self is None:
            return 0
        else:
            left_size  = self.__left_child.get_chromossome_size() \
                        if self.__left_child  is not None else 0
            right_size = self.__right_child.get_chromossome_size() \
                        if self.__right_child is not None else 0
            return left_size + right_size + 1

    def search(self, index):
        curr  = self
        stack = []
        count = 0
        node_found = False

        while not node_found:
            if curr is not None:
                stack.append(curr)
                curr = curr.get_left_child()
            else:
                if len(stack) > 0:
                    curr = stack.pop()
                    if count == index:
                        node_found = True
                        return curr
                    curr = curr.get_right_child()
                    count += 1
                else:
                    node_found = True

    def replace_chromossome(self, chromo, new_subtree):
        if self is None:
            return

        if self.__left_child == chromo:
            chromo.__left_child = new_subtree
            return
        else:
            if self.__left_child is not None:
                self.__left_child.replace_chromossome(chromo, new_subtree)
        if self.__right_child == chromo:
            self.__right_child = new_subtree
            return
        else:
            if self.__right_child is not None:
                self.__right_child.replace_chromossome(chromo, new_subtree)
        return

    def chromossome_tree_str(self):
        if self is not None:
            left_side_str  = str(self.__left_child.chromossome_tree_str()) \
                            if self.__left_child is not None else ''
            right_side_str = str(self.__right_child.chromossome_tree_str()) \
                            if self.__right_child is not None else ''
            utils = Utils()
            if utils.is_operator_binary(str(self)) or utils.is_terminal(str(self)):
                return '(' + left_side_str + ' ' +  str(self) + ' ' + right_side_str + ')'
            else:
                return '( ' + str(self) + ' ' + left_side_str + ' )'
        else:
            return ' '

    def resize_tree(self, depth):
        if depth > 0:
            if self.__left_child is not None:
                self.__left_child.resize_tree(depth - 1)
            if self.__right_child is not None:
                self.__right_child.resize_tree(depth - 1)
        else:
            print('[+] Prunning tree.')
            if Utils().is_terminal(self.__symbol):
                self.__left_child  = None
                self.__right_child = None
            else:
                self = None
        
    @classmethod
    def gen_random_chromossome(cls, depth, method):
        utils = Utils()
        arg1 = None
        arg2 = None

        # Provide equal probability of choosing a terminal and an operator
        choosing_terminal = utils.get_random_probability() <= 0.5

        if depth == 0 or (method == 'grow' and choosing_terminal):
            expr = utils.get_terminal()
        else:        
            expr = utils.get_function()
            arg1 = cls.gen_random_chromossome(depth - 1, method)
            if utils.is_operator_binary(expr):
                arg2 = cls.gen_random_chromossome(depth - 1, method)

        return Chromossome(expr, arg1, arg2)

