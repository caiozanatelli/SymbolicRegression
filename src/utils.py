import random

class GeneticOperators:
    pass

class Singleton(type):

    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

class Utils(object):
    __metaclass__ = Singleton

    __binary_ops  = None
    __unary_ops   = None
    __variables   = None

    ADD_OP_SYMBOL = '+'
    SUB_OP_SYMBOL = '-'
    DIV_OP_SYMBOL = '/'
    MUL_OP_SYMBOL = '*'
    COS_OP_SYMBOL = 'cos'
    SIN_OP_SYMBOL = 'sin'

    MIN_DEPTH     = 3

    def __init__(self):
        self.__init_operands()

    def __init_operands(self):
        self.__binary_ops = ['+', '-', '*', '/']
        self.__unary_ops  = ['sin', 'cos']
        self.set_variables(3)

    def set_variables(self, nvariables):
        self.__variables  = []
        for i in xrange(nvariables):
            self.__variables.append('X' + str(i))

    def get_variables(self):
        return self.__variables

    def get_operators(self):
        return self.__binary_ops + self.__unary_ops

    def is_operator(self, x):
        return x in self.__binary_ops + self.__unary_ops

    def is_operator_unary(self, op):
        return op in self.__unary_ops

    def is_operator_binary(self, op):
        return op in self.__binary_ops

    def is_variable(self, x):
        return x in self.__variables

    def is_constant(self, x):
        return x not in (self.__binary_ops + self.__unary_ops) and float(x) <= 1

    def is_terminal(self, x):
        return self.is_variable(x) or self.is_constant(x)

    def get_terminal(self):
        choosing_constant = self.get_random_probability()
        if choosing_constant:
            return self.get_constant()
        return self.__variables[random.randint(0, len(self.__variables) - 1)]

    def get_function(self):
        len_binary = len(self.__binary_ops)
        len_unary  = len(self.__unary_ops)
        index = random.randint(0, len_binary + len_unary - 1)

        if index < len_binary:
            return self.__binary_ops[index]
        else:
            return self.__unary_ops[len_binary + len_unary - index - 1]
   
    def get_constant(self):
        return random.random()

    def get_random_probability(self):
        return random.random()

if __name__ == '__main__':
    utils1 = Utils()
    print(utils1.get_operands())

    utils2 = Utils()
    print(utils2.get_operands())

    utils3 = Utils()
    print(utils3.get_operands())