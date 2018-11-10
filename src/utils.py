import random

class Singleton(type):

    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

class Utils(object):
    __metaclass__ = Singleton

    ADD_OP_SYMBOL  = '+'
    SUB_OP_SYMBOL  = '-'
    DIV_OP_SYMBOL  = '/'
    MUL_OP_SYMBOL  = '*'
    POW_OP_SYMBOL  = 'pow'
    SQRT_OP_SYMBOL = 'sqrt'
    COS_OP_SYMBOL  = 'cos'
    SIN_OP_SYMBOL  = 'sin'
    LOG_OP_SYMBOL  = 'log'

    __binary_ops  = None
    __unary_ops   = None
    __variables   = None

    def __init__(self, seed=None, nvariables=None):
        self.__init_operators()
        if seed is not None:
            random.seed(seed)
        if nvariables is not None:
            self.set_variables(nvariables)

    def __init_operators(self):
        self.__binary_ops = ['+', '-', '*', '/']
        #self.__unary_ops  = []
        self.__unary_ops  = ['log', 'sqrt', 'pow']

    def set_variables(self, nvariables):
        self.__variables  = []
        for i in xrange(nvariables):
            self.__variables.append('X' + str(i))

    def get_variables(self):
        return self.__variables

    def get_operators(self):
        return self.__binary_ops + self.__unary_ops

    def get_random_node(self):
        return random.choice(self.__variables + self.__binary_ops + self.__unary_ops)

    def is_operator(self, x):
        return x in self.__binary_ops + self.__unary_ops

    def is_operator_unary(self, op):
        return op in self.__unary_ops

    def is_operator_binary(self, op):
        return op in self.__binary_ops

    def is_variable(self, x):
        return x in self.__variables

    def is_constant(self, x):
        return not self.is_operator(x) and not self.is_variable(x)

    def is_terminal(self, x):
        return self.is_variable(x) or self.is_constant(x)

    def get_terminal(self):
        choosing_constant = self.get_random_probability() < 0.5
        if choosing_constant:
            return self.get_constant()
        return 'X' + str(random.randint(0, len(self.__variables) - 1))

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

    def get_randint(self, start, end):
        return random.randint(start, end)
