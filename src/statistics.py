class Statistics:

    def __init__(self, best=None, worst=None, avg_fitness=None):
        self.clear()

    def clear(self):
        self.__curr_generation  = 0
        self.__best_individual  = None
        self.__worst_individual = None
        self.__avg_fitness      = 0.0
        self.__nrepeated_individuals     = 0
        self.__ncross_best_than_parents  = 0
        self.__ncross_worst_than_parents = 0

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

    def set_ncross_best_than_parents(self, number):
        self.__ncross_best_than_parents = number

    def get_ncross_best_than_parents(self):
        return self.__ncross_best_than_parents

    def incr_ncross_best_than_parents(self):
        self.__ncross_best_than_parents += 1

    def incr_ncross_worst_than_parents(self):
        self.__ncross_worst_than_parents += 1

    def set_ncross_worst_than_parents(self, number):
        self.__ncross_worst_than_parents = number

    def get_ncross_worst_than_parents(self):
        return self.__ncross_worst_than_parents

    def statistics_str(self):
        return  '[+] Generation:      ' + str(self.__curr_generation) + '\n' \
                + '[+] Average Fitness: ' + str(self.__avg_fitness) + '\n' \
                + '[+] Best Fitness:    ' + str(self.__best_individual.get_fitness())  + '\n' \
                + '[+] Worst Fitness:   ' + str(self.__worst_individual.get_fitness()) + '\n' \
                + '[+] Number of repeated invididuals: ' + str(self.__nrepeated_individuals) + '\n' \
                + '[+] Number of crossover-generated individuals that are better then their parents: ' \
                    + str(self.__ncross_best_than_parents) + '\n' \
                + '[+] NUmber of crossover-generated individuals that are worse than their parents: ' \
                    + str(self.__ncross_worst_than_parents) + '\n' \
                + '----------------------------------\n'

    def get_stats_csv_fmt(self):
        return  str(self.__curr_generation) + ',' + str(self.__avg_fitness) + ',' \
                + str(self.__best_individual.get_fitness()) + ',' + str(self.__worst_individual.get_fitness()) \
                + ',' + str(self.__nrepeated_individuals) + ',' + str(self.__ncross_best_than_parents) + ',' \
                + str(self.__ncross_worst_than_parents)

