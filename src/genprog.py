from chromossome import Chromossome
from individual import Individual
from population import Population
from statistics import Statistics
from utils import Utils
import collections
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
        self.__stats = Statistics()

    def train(self, dataset):
        self.__population = Population(self.__pop_size, self.__max_depth)
        stats = self.__population.calculate_fitness(dataset)
        fitness = stats.get_avg_fitness()
        best = stats.get_best_individual()
        worst = stats.get_worst_individual()

        stats.print_statistics()

        for generation in range(self.__ngenerations):
            # Calculate the number of repeated individuals in the population
            unique_chromos = list(collections.Counter(indiv.function_str() 
                                for indiv in self.__population.get_individuals()))
            stats.set_nrepeated_individuals(self.__pop_size - len(unique_chromos))

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

