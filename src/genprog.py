import numpy as np
import random

class GeneticProgramming:
    __args = None

    def __init__(self, args):
        self.__args = args

    def train(self, dataset):
        max_depth  = self.__args.max_depth
        pop_size   = self.__args.pop_size
        cross_prob = self.__args.cross_prob
        mut_prob   = self.__args.mut_prob
        seed       = self.__args.seed

    def test(self, dataset):
        pass

    def __tournament_selection(self, population, tour_size):
        """
        Perform a tournament selection among the elements of the population.

        Arguments:
            population: list of individual objects that represent the population.
            tour_size: integer representing the tournament size.

        Returns:
            [int] -- the index of the element that won the tournament
        """
        chosen_elems = []
        for i in range(tour_size):
            chosen_elems.append(0, self.get_population_size() - 1)

        best_elem_index   = 0
        fitness_best_elem = float('inf')

        for i in chosen:
            curr_fitness = self.get_individual_at(i)
            if curr_fitness <= fitness_best_elem:
                fitness_best_elem = curr_fitness
                best_elem_index   = i

        return best_elem_index
