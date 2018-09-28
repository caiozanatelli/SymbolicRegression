class Statistics:

    def __init__(self, best=None, worst=None, avg_fitness=None):
        self.__curr_generation  = 0
        self.__best_individual  = best
        self.__worst_individual = worst
        self.__avg_fitness      = avg_fitness
        self.__nrepeated_individuals   = 0
        self.__ncross_best_individuals = 0

    def set_current_generation(self, generation):
        self.__curr_generation = generation

    def get_current_generation(self):
        return self.__curr_generation

    def get_best_individual(self):
        return self.__best_individual

    def set_best_individual(self, best):
        self.__best_individual = best

    def get_worst_individual(self):
        return self.__worst_individual

    def set_worst_individual(self, worst):
        self.__worst_individual = worst

    def get_avg_fitness(self):
        return self.__avg_fitness

    def set_avg_fitness(self, avg_fitness):
        self.__avg_fitness = avg_fitness

    def set_nrepeated_individuals(self, number):
        self.__nrepeated_individuals = number

    def get_nrepeated_individuals(self):
        return self.__nrepeated_individuals

    def set_ncross_best_individuals(self, number):
        self.__ncross_best_individuals = number

    def get_ncross_best_individuals(self):
        return self.__ncross_best_individuals

    def print_statistics(self):
        print('----------------------------------')
        print('[+] Average Fitness: ' + str(self.__avg_fitness))
        print('[+] Best Fitness:    ' + str(self.__best_individual.get_fitness()))
        print('[+] Worst Fitness:   ' + str(self.__worst_individual.get_fitness()))
        print('----------------------------------')
