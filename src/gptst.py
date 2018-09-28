from chromossome import Chromossome
from individual import Individual
from utils import Utils
from ioutils import IOUtils
from population import Population

if __name__ == '__main__':
    dataset_input = IOUtils().read_csv('../datasets/synth1/synth1-train.csv')

    #chromo = Chromossome.gen_random_chromossome(7, 'grow')
    #individual = Individual(chromo)
    #print('\n\n\n')
    #print(individual.function_str())

    #print('\n\nFitness: ' + str(individual.calculate_fitness(dataset_input)))
    SEED = 1
    NVARIABLES = 2

    Utils(SEED, NVARIABLES)

    population = Population(30, 7)
    individuals = population.get_individuals()

    rows = len(dataset_input)
    avg_dataset_output = 0.0        
    for i in range(rows):
        avg_dataset_output += dataset_input[i][-1]
    avg_dataset_output /= rows

    #for i in range(len(individuals)):
        #print('----------------------------------------------------------------------------------')
        #print('                           INDIVIDUAL ' + str(i))
        #print('----------------------------------------------------------------------------------')
        #print(individuals[i].function_str())
    #    print('[+] Fitness: ' + str(individuals[i].calculate_fitness(dataset_input, avg_dataset_output)))
        #print('\n')

    population.calculate_population_fitness(dataset_input)