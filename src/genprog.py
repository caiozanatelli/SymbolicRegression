from chromossome import Chromossome
from individual import Individual
from population import Population
from statistics import Statistics
from ioutils import IOUtils
from utils import Utils
import collections
import copy
import sys
import numpy as np
import random
import gc

class GeneticProgramming:
    __population = None
    __fitness    = float('inf')
    __best_indiv = None

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

        self.__max_chromo_size = (2 ** (args.max_depth + 1)) -1

        Utils(args.seed, args.nvariables)
        IOUtils().open_output_file(args.out)

    def train(self, dataset):
        print('[+] Initializing population.')

        self.__population = Population(self.__pop_size, self.__max_depth)
        stats = Statistics()
        utils   = Utils()
        ioutils = IOUtils()
        avg_dataset_output = sum(dataset[i][-1] for i in range(len(dataset))) / len(dataset)
        self.__population.calculate_fitness(dataset, avg_dataset_output)

        for generation in range(1, self.__ngenerations + 1):
            print('[+] Generation: ' + str(generation) + '/' + str(self.__ngenerations))

            best_indiv, worst_indiv, avg_pop_fitness = self.__population.get_stats()
            self.__best_indiv = copy.deepcopy(best_indiv)

            stats.set_current_generation(generation)
            stats.set_best_individual(best_indiv)
            stats.set_worst_individual(worst_indiv)
            stats.set_avg_fitness(avg_pop_fitness)

            # Calculate the number of repeated individuals in the population
            unique_chromos = list(collections.Counter(indiv.function_str() 
                                    for indiv in self.__population.get_individuals()))
            stats.set_nrepeated_individuals(self.__pop_size - len(unique_chromos))

            # Write the current population's statistics to the output file
            ioutils.write_output(stats.statistics_str())
            ioutils.write_log(stats.get_stats_csv_fmt() + '\n')
            print(stats.get_stats_csv_fmt())
            stats.clear()

            next_population = Population()
            next_population.set_max_depth(self.__max_depth)

            if self.__enbl_elitism:
                next_population.add_individual(best_indiv)

            # Garanteeing that the new population will be completely renewed
            while next_population.get_size() < self.__pop_size:
                try:
                    index_parent_chromo1 = self.__tournament_selection()
                    parent1 = self.__population.get_individual_at(index_parent_chromo1)

                    random_prob = utils.get_random_probability()
                    
                    # Perform the crossover based on its probability
                    if random_prob <= self.__cross_prob:
                        # Choose the parents
                        index_parent_chromo2 = self.__tournament_selection()
                        parent2 = self.__population.get_individual_at(index_parent_chromo2)

                        # Perform the crossover itself and calculate the children and parents' fitnesses
                        new_child1, new_child2 = self.__crossover(parent1, parent2)
                        avg_fitness_parents = (parent1.get_fitness() + parent2.get_fitness()) / 2
                        fitness_child1 = new_child1.calculate_fitness(dataset, avg_dataset_output)
                        fitness_child2 = new_child2.calculate_fitness(dataset, avg_dataset_output)

                        # Update the statistics after the crossover
                        if fitness_child1 < avg_fitness_parents:
                            stats.incr_ncross_worst_than_parents()
                        elif fitness_child1 > avg_fitness_parents:
                            stats.incr_ncross_best_than_parents()
                        if fitness_child2 < avg_fitness_parents:
                            stats.incr_ncross_worst_than_parents()
                        elif fitness_child2 > avg_fitness_parents:
                            stats.incr_ncross_best_than_parents()

                        # Add the children generated by crossover to the next population
                        next_population.add_individual(new_child1)
                        if next_population.get_size() < self.__pop_size:
                            next_population.add_individual(new_child2)

                    # Perform the mutation based on its probability
                    elif random_prob <= self.__cross_prob + self.__mut_prob:
                        new_child1 = parent1.mutate()
                        fitness_child1 = new_child1.calculate_fitness(dataset, avg_dataset_output)
                        next_population.add_individual(new_child1)
                except Exception as e:
                    pass

            self.__population = next_population            

    def test(self, dataset):
        print('Minimum Error:      ' + str(self.__best_indiv.calculate_fitness(dataset)))
        print('Generated Function: ' + self.__best_indiv.function_str())
        ioutils = IOUtils()
        ioutils.write_log(str(self.__best_indiv.calculate_fitness(dataset)) + '\n')

    def __tournament_selection(self):
        """
        Perform a tournament selection among the elements of the population.

        Arguments:
            population: list of individual objects that represent the population.
            tour_size: integer representing the tournament size.

        Returns:
            [int] -- the index of the element that won the tournament
        """
        chosen_elems = []
        for i in range(self.__tour_size):
            chosen_elems.append(Utils().get_randint(0, self.__pop_size - 1))

        best_elem_index   = 0
        fitness_best_elem = float('inf')

        for i in chosen_elems:
            curr_fitness = self.__population.get_individual_at(i).get_fitness()
            if curr_fitness <= fitness_best_elem:
                fitness_best_elem = curr_fitness
                best_elem_index   = i

        return best_elem_index

    def __crossover(self, parent1, parent2):
        utils = Utils()

        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)

        size_parent1 = parent1.get_genotype().get_chromossome_size()
        size_parent2 = parent2.get_genotype().get_chromossome_size()
        cross_index_parent1 = utils.get_randint(0, size_parent1 - 1)
        cross_point_child1  = child1.get_genotype().search(cross_index_parent1)
        cross_point_child1_size = cross_point_child1.get_chromossome_size()
        valid_range_parent1 = self.__max_chromo_size - (size_parent1 - cross_point_child1_size)
        valid_range_parent2 = utils.get_randint(0, valid_range_parent1 - 1)

        cross_index_parent2 = 0
        if valid_range_parent2 <= size_parent2:
            cross_index_parent2 = valid_range_parent2
        else:
            cross_index_parent2 = utils.get_randint(0, size_parent2 - 1)

        cross_point_child2 = child2.get_genotype().search(cross_index_parent2)

        #valid_range_parent2 = utils.randint(0, Individual.MAX_CHROMO_SIZE - size_parent1)
        #valid_range_parent1 = Individual.MAX_CHROMO_SIZE - size_parent1


        #cross_index_parent2 = valid_range_parent2 

        #cross_point_child1 = child1.get_genotype().search(Utils().get_randint(0, size_parent1 / 2 ))
        #cross_point_child2 = child2.get_genotype().search(Utils().get_randint(0, size_parent2 / 2))

        if child1 == cross_point_child1:
            child1 = cross_point_child2
        else:
            child1.get_genotype().replace_chromossome(cross_point_child1, cross_point_child2)

        if child2 == cross_point_child2:
            child2 = cross_point_child1
        else:
            child2.get_genotype().replace_chromossome(cross_point_child2, cross_point_child1)

        child1_chromo = child1.get_genotype()
        child2_chromo = child1.get_genotype()

        return (child1, child2)
