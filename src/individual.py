from utils import Utils
import numpy as np
import math
import sys

class Individual:

    def __init__(self, root_chromo=None):
        self.__genotype = root_chromo
        self.__fitness  = None

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
        self.__fitness = 0.0
        sum_diff       = 0.0
        norm_factor    = 0.0
        for row in dataset_input:
            #print('----> ROW: ' + str(row))
            try:
                res_eval = self.eval(self.__genotype, row)
                sum_diff += (row[-1] - res_eval) ** 2
            except Exception:
                sum_diff = sys.maxint
        
            norm_factor += (row[-1] - avg_dataset_output) ** 2

        self.__fitness = math.sqrt((sum_diff / norm_factor))
        print('[+] Fitness: ' + str(self.__fitness))
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
            elif str_chromo == Utils.SIN_OP_SYMBOL:
                return math.sin(self.eval(left, xarray))
            elif str_chromo == Utils.COS_OP_SYMBOL:
                return math.cos(self.eval(left, xarray))
        # The current node is a variable
        elif utils.is_variable(str_chromo):
            index = int(str_chromo[1:])
            #print('--------> VARIABLE: X' + str(index) + '       VALUE: ' + str(xarray[index]))
            return xarray[index] if index < len(xarray) - 1 else 0
        # The current node is a constant
        else:
            return float(str_chromo) # TODO: CHECK THIS LATER!

    def mutate(self):
        """
        Perform the mutation genetic operator to a chromossome.
        """
        pass

    def crossover(self):
        pass

    def function_str(self):
        return self.__genotype.chromossome_tree_str()

    def get_genotype(self):
        return self.__genotype