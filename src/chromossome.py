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
        if self is not None:
            return str(self.__symbol)
        return ' '

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
            #return '( ' + str(self) + ' ' + left_side_str + ' ' + right_side_str + ' )'
        else:
            return ' '

    def get_chromossome_size(self):
        """
        Calculate the size of a chromossome recursively.

        Returns:
            [int] -- the size of the chromossome.
        """
        return self.__left_child.get_chromossome_size() + \
                self.__right_child.get_chromossome_size() + 1 if self is None else 0

    @classmethod
    def gen_random_chromossome(cls, depth, method):

        #print('----> Recursion')
        #print('Max Depth: ' + str(depth))

        utils = Utils()
        arg1 = None
        arg2 = None

        # Provide equal probability of choosing a terminal and an operator
        choosing_terminal = utils.get_random_probability() <= 0.5

        if depth == 0 or (method == 'grow' and choosing_terminal):
            expr = utils.get_terminal()
            #print('[+] Terminal: ' + str(expr))
        else:        
            expr = utils.get_function()
            arg1 = cls.gen_random_chromossome(depth - 1, method)
            if utils.is_operator_binary(expr):
                arg2 = cls.gen_random_chromossome(depth - 1, method)

        #print('[+] Expression: ' + str(arg1) + ' ' + str(expr) + ' ' + str(arg2))

        return Chromossome(expr, arg1, arg2)

