from chromossome import Chromossome
from individual import Individual
from utils import Utils
from population import Population

if __name__ == '__main__':
    chromo = Chromossome.gen_random_chromossome(2, 'grow')
    individual = Individual(chromo)
    print('\n\n\n')
    print(individual.function_str())

    print('\n\nFitness: ' + str(individual.calculate_fitness()))
    