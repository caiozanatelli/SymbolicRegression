from utils import Utils
from chromossome import Chromossome
import numpy as np
import copy
import math
import sys

class Individual:

    def __init__(self, max_depth, root_chromo=None):
        self.__genotype  = root_chromo
        self.__max_depth = max_depth
        self.__fitness   = float('inf')
        self.__max_chromo_size = (2 ** (max_depth + 1)) -1

        if not root_chromo is None:
            self.__size = root_chromo.get_chromossome_size()

    def calculate_fitness(self, dataset_input, avg_dataset_output=None):
        """ 
        Fitness calculation via Normalized Root Mean Square Error (NRMSE)

        Arguments:
            dataset_input{numpy.array} -- the dataset input for evalution, that is,
            the function's inputs and outputs

        Returns:
            A list of floating points indicating the individual fitness for each
            input.
        """
        rows = len(dataset_input)

        if avg_dataset_output is None:
            avg_dataset_output = sum(dataset_input[i][-1] for i in range(rows)) / rows

        self.__fitness = 0.0
        sum_diff       = 0.0
        norm_factor    = 0.0
        for row in dataset_input:
            try:
                res_eval = self.eval(self.__genotype, row)
                sum_diff += (row[-1] - res_eval) ** 2
            except Exception:
                sum_diff = sys.maxint
        
            norm_factor += (row[-1] - avg_dataset_output) ** 2

        if self.__genotype.get_chromossome_size() > self.__max_chromo_size:
            self.__fitness = sys.maxint
        else:
            self.__fitness = math.sqrt((sum_diff / norm_factor))

        return self.__fitness

    def get_fitness(self):
        return self.__fitness

    def eval(self, curr_chromo, xarray):
        """
        Evaluates the function representation (chromossome) on the input array x.

        Arguments:
            x{numpy.array(float)} -- input values for the function evaluation.

        Returns:
            The value obtained in the evaluation.
        """
        utils = Utils()
        str_chromo = str(curr_chromo)

        # The current node is an operator
        if utils.is_operator(str_chromo):
            left  = curr_chromo.get_left_child()
            right = curr_chromo.get_right_child()

            if str_chromo == utils.ADD_OP_SYMBOL:
                return self.eval(left, xarray) + self.eval(right, xarray)
            elif str_chromo == Utils.SUB_OP_SYMBOL:
                return self.eval(left, xarray) - self.eval(right, xarray)
            elif str_chromo == Utils.MUL_OP_SYMBOL:
                return self.eval(left, xarray) * self.eval(right, xarray)
            elif str_chromo == Utils.DIV_OP_SYMBOL:
                # Safe division: return 1 if the denominator is 0
                numerator   = self.eval(left, xarray)
                denominator = self.eval(right, xarray)
                return numerator / denominator if denominator != 0 else 0
            elif str_chromo == Utils.POW_OP_SYMBOL:
                return self.eval(left, xarray) ** 2
            elif str_chromo == Utils.SQRT_OP_SYMBOL:
                return math.sqrt(self.eval(left, array))
            elif str_chromo == Utils.LOG_OP_SYMBOL:
                return math.log(self.eval(left, array))
            elif str_chromo == Utils.SIN_OP_SYMBOL:
                return math.sin(self.eval(left, xarray))
            elif str_chromo == Utils.COS_OP_SYMBOL:
                return math.cos(self.eval(left, xarray))
        # The current node is a variable
        elif utils.is_variable(str_chromo):
            index = int(str_chromo[1:])
            return xarray[index] if index < len(xarray) - 1 else 0
        # The current node is a constant
        else:
            return float(str_chromo)

    def mutate(self):
        """
        Perform the mutation genetic operator to a chromossome by replacing a node's subtree
        by another one generated randomly.

        Returs:
            A Chromossome object representing the mutated node.
        """
        utils = Utils()
        copy_chromo = copy.deepcopy(self)
        #copy_chromo = self
        tree_size   = self.__genotype.get_chromossome_size()
        tree_depth  = math.floor(math.log(tree_size, 2))

        mut_index   = utils.get_randint(0, tree_size - 1)
        mut_chromo  = copy_chromo.get_genotype().search(mut_index)
        mut_chromo_size  = copy_chromo.get_genotype().get_chromossome_size()
        mut_chromo_depth = math.floor(math.log(mut_chromo_size, 2))
        mut_max_depth   = self.__max_depth - (tree_size - mut_chromo_depth)

        # Get a random new operator or terminal for the chromo being mutated
        new_chromo_symbol = utils.get_random_node()
        left  = None
        right = None

        # The chosen node is a variable 
        if utils.is_variable(new_chromo_symbol):
            mut_chromo.set_symbol(new_chromo_symbol)
        # The chosen node is a function
        else:
            mut_chromo.set_symbol(new_chromo_symbol)
            new_subtree_depth = utils.get_randint(2, mut_max_depth - 1)
            left  = Chromossome.gen_random_chromossome(new_subtree_depth, 'full')
            right = None if utils.is_operator_unary(new_chromo_symbol) \
                    else Chromossome.gen_random_chromossome(new_subtree_depth, 'full')
        mut_chromo.set_left_child(left)
        mut_chromo.set_right_child(right)

        return copy_chromo

    def function_str(self):
        return self.__genotype.chromossome_tree_str()

    def get_genotype(self):
        return self.__genotype

    def get_fitness(self):
        return self.__fitness