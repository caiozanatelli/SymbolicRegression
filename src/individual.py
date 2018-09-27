from utils import Utils
import math

class Individual:

    def __init__(self, root_chromo=None):
        self.__genotype = root_chromo
        self.__fitness  = None

    def calculate_fitness(self, dataset_input=None, avg_dataset_output=None):
        """ 
        Fitness calculation via Normalized Root Mean Square Error (NRMSE)

        Arguments:
            dataset_input{numpy.array} -- the dataset input for evalution, that is,
            the function's inputs and outputs

        Returns:
            A list of floating points indicating the individual fitness for each
            input.
        """
        #dataset_input = [[-1.235928614240245,-1.3641055948703154,6.515718683072601]]
        dataset_input = [[2.0,5.0,10.0]]
        rows = len(dataset_input)

        avg_dataset_output = 0
        for i in range(rows):
            avg_dataset_output += dataset_input[i][-1]

        avg_dataset_output /= rows

        self.__fitness = []
        sum_diff = 0
        norm_factor = 0
        index = 0

        for row in dataset_input:
            res_eval = self.eval(self.__genotype, row)
            sum_diff += (row[-1] - res_eval) ** 2
            norm_factor += (row[-1] - avg_dataset_output) ** 2
            if norm_factor == 0:
                norm_factor = 1
            index += 1

            self.__fitness.append(math.sqrt((sum_diff / norm_factor)))

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
                numerator   = self.eval(left, xarray)
                denominator = self.eval(right, xarray)
                return numerator / denominator if denominator != 0 else 0
            elif str_chromo == Utils.SIN_OP_SYMBOL:
                return math.sin(self.eval(left, xarray))
            elif str_chromo == Utils.COS_OP_SYMBOL:
                return math.cos(self.eval(left, xarray))

        # The current node is a variable
        elif utils.is_variable(str_chromo):
            index = int(str(chromo)[1:])
            return xarray[index]
        # The current node is a constant
        else:
            return utils.get_constant() # TODO: CHECK THIS LATER!


    def mutate(self):
        pass

    def crossover(self):
        pass

    def function_str(self):
        return self.__genotype.chromossome_tree_str()

    def get_genotype(self):
        return self.__genotype