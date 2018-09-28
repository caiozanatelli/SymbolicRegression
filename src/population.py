from chromossome import Chromossome
from individual import Individual
from multiprocessing import Process

class Population:
    __individuals = None
    __max_depth   = None

    def __init__(self, population_size, max_depth):
        self.__max_depth        = max_depth
        self.__best_individual  = None
        self.__worst_individual = None
        self.__avg_fitness      = 0.0
        self.__nrepeated_individuals   = 0
        self.__ncross_best_individuals = 0
        self.__population_size = population_size
        # Generate an initial population
        self.initialize_population()

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

    def get_population_size(self):
        return self.__population_size

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

    def calculate_fitness(self, xarray):
        pop_size = len(self.__individuals)
        rows = len(xarray)
        avg_dataset_output = sum(xarray[i][-1] for i in range(rows)) / rows

        self.__avg_fitness = 0.0
        worst_fitness = 0.0
        best_fitness  = float('inf')

        for indiv in self.__individuals:
            indiv_fitness = indiv.calculate_fitness(xarray, avg_dataset_output)
            self.__avg_fitness += indiv_fitness
                        
            if indiv_fitness < best_fitness:
                self.__best_individual  = indiv
                best_fitness = indiv_fitness

            if indiv_fitness > worst_fitness:
                self.__worst_individual = indiv
                worst_fitness = indiv_fitness

        self.__avg_fitness /= pop_size

        #processes = [Process(target=self.__individuals[i].calculate_fitness, args=(xarray, avg_dataset_output,)) 
        #            for i in range(len(self.__individuals))]

        # Run all the processes
        #for p in processes:
        #    p.start()
        # Wait all the processes to finish
        #for p in processes:
        #    p.join()

        #sum_fitness = sum(indiv.get_fitness() for indiv in self.__individuals) / len(self.__individuals)
        #for i in self.__individuals:
        #    print(i.get_fitness())

        return (self.__avg_fitness, self.__best_individual, self.__worst_individual)
        