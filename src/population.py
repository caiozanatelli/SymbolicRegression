from multiprocessing import Process

class Population:
    __individuals = []

    def __init__(self):
        self.__best_fitness = 0.0
        self.__avg_fitness  = 0.0
        self.__nrepeated_individuals = 0
        self.__ncross_best_individuals = 0

    def initialize_population(self):
        pass

    def calculate_population_fitness(self, xarray):
        processes = [Process(target=indiv.calculate_fitness, args=(xarray,)) 
                    for indiv in self.__individuals]

        # Run all the processes
        for p in processes:
            p.start()
        # Wait all the processes to finish
        for p in processes:
            p.join()

        return (self.__best_fitness, self.__avg_fitness, 
                self.__nrepeated_individuals, self.__ncross_best_individuals)
        