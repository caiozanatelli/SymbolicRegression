from chromossome import Chromossome
from individual import Individual
from population import Population
from utils import Utils
import numpy as np
import random

class GeneticProgramming:
    __population = None
    __fitness    = float('inf')

    def __init__(self, args):
        self.__max_depth    = args.max_depth
        self.__pop_size     = args.pop_size
        self.__cross_prob   = args.cross_prob
        self.__mut_prob     = args.mut_prob
        self.__seed         = args.seed
        self.__tour_size    = args.tour_size
        self.__ngenerations = args.ngen
        self.__enbl_elitism = args.elitism
        self.__nvariables   = args.nvariables

        Utils(args.seed, args.nvariables)

    def train(self, dataset):
        self.__population = Population(self.__pop_size, self.__max_depth)
        avg_fitness, best, worst = self.__population.calculate_fitness(dataset)

        print('\n')
        print('[+] Average Fitness: ' + str(avg_fitness))
        print('[+] Best Fitness:    ' + str(best.get_fitness()))
        print('[+] Worst Fitness:   ' + str(worst.get_fitness()))
        print('')

        print('[+] Best individual:  ' + str(best.function_str()))
        print('\n')
        print('[+] Worst individual: ' + str(worst.function_str()))
        print('')

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

