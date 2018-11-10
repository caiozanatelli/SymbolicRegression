from chromossome import Chromossome
from individual import Individual
from statistics import Statistics
from multiprocessing import Process
import copy

class Population:
    __individuals = None
    __max_depth   = None

    def __init__(self, population_size=None, max_depth=None):
        # Generate an initial population
        self.__max_depth       = max_depth
        self.__population_size = population_size

        if population_size is not None and max_depth is not None:
            self.initialize_population()
        else:
            self.__individuals = []
        
    def set_max_depth(self, max_depth):
        self.__max_depth = max_depth

    def add_individual(self, individual):
        self.__individuals.append(individual)

    def get_size(self):
        return len(self.__individuals)

    def initialize_population(self):
        """
        Initialization of the population. The method used in this case is the Ramped Half-Half,
        but the encapsulation is applied in order to provide easy method switch if needed.

        Returns:
            A list of Individual objects generated in the process.
        """
        return self.__gen_ramped_half_half()

    def get_individuals(self):
        return self.__individuals

    def get_individual_at(self, index):
        return self.__individuals[index] if index >= 0 and index < len(self.__individuals) else None

    #def get_population_size(self):
    #    return self.__population_size

    def __gen_ramped_half_half(self):
        """ 
        Generate a population of N random individuals using the Ramped Half Half method.
        In other words, we create a population containing N/2 individuals composed of a
        full chromossome tree and N/2 with no fullness restriction. At each round, we 
        set the depth to be 1, 2, ..., MAX-DEPTH.

        Returns:
            A list of Individual objects generated randomly following the Ramped Half Half
            method.
        """
        self.__individuals = []
        half_size = self.__population_size / 2
        for i in range(half_size):
            max_depth = self.__max_depth % (i + 1)
            self.__individuals.append(Individual(self.__max_depth, 
                                        Chromossome.gen_random_chromossome(max_depth, 'full')))
            self.__individuals.append(Individual(self.__max_depth, 
                                        Chromossome.gen_random_chromossome(max_depth, 'grow')))
        return self.__individuals

    def get_stats(self):
        avg_fitness   = 0.0
        best_fitness  = float('inf')
        worst_fitness = 0.0
        best_individual  = None
        worst_individual = None

        pop_size = len(self.__individuals)

        for indiv in self.__individuals:
            indiv_fitness = indiv.get_fitness()
            #indiv_fitness = 1
            avg_fitness  += indiv_fitness

            if indiv_fitness < best_fitness:
                best_individual = indiv
                best_fitness = indiv_fitness
            if indiv_fitness > worst_fitness:
                worst_individual = indiv
                worst_fitness = indiv_fitness
        avg_fitness /= pop_size

        return (best_individual, worst_individual, avg_fitness)


    def calculate_fitness(self, xarray, avg_dataset_output=None):
        pop_size = len(self.__individuals)
        rows = len(xarray)

        if avg_dataset_output is None:
            avg_dataset_output = sum(xarray[i][-1] for i in range(rows)) / rows

        avg_fitness   = 0.0
        worst_fitness = 0.0
        best_fitness  = float('inf')
        best_individual  = None
        worst_individual = None

        for indiv in self.__individuals:
            indiv_fitness = indiv.calculate_fitness(xarray, avg_dataset_output)
            avg_fitness += indiv_fitness
                        
            if indiv_fitness < best_fitness:
                best_individual = indiv
                best_fitness = indiv_fitness
            if indiv_fitness > worst_fitness:
                worst_individual = indiv
                worst_fitness = indiv_fitness
        avg_fitness /= pop_size

        return (copy.deepcopy(best_individual), copy.deepcopy(worst_individual), avg_fitness)
