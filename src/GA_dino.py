import numpy
import dinogame.ga_setup as ga

# Number of the weights we are looking to optimize.
num_weights = 3

"""
Genetic algorithm parameters:
    Mating pool size
    Population size
"""
sol_per_pop = 8
num_parents_mating = 4

# Defining the population size.
pop_size = (sol_per_pop, num_weights)  # The population will have sol_per_pop chromosome where each chromosome has
# num_weights genes.
# Creating the initial population.
new_population = numpy.random.uniform(low=-4.0, high=4.0, size=pop_size)
print(new_population)


num_generations = 1
for generation in range(num_generations):
    print("Generation : ", generation)
    # Measuring the fitness of each chromosome in the population.
    print(f'#Measuring the fitness of each chromosome in the population.')

    fitness = ga.cal_pop_fitness(new_population)

    # dump the best solution into file
    # file =

    # Selecting the best parents in the population for mating.
    print(f'# Selecting the best parents in the population for mating.')

    parents = ga.select_mating_pool(new_population, fitness, num_parents_mating)

    # Generating next generation using crossover.
    offspring_crossover = ga.crossover(parents,
                                       offspring_size=(pop_size[0]-parents.shape[0], num_weights))

    # Adding some variations to the offspring using mutation.
    offspring_mutation = ga.mutation(offspring_crossover)

    # Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

    # The best result in the current iteration.
    print("Best result : ", numpy.max(fitness))
    print(new_population)

# Getting the best solution after iterating finishing all generations.
# At first, the fitness is calculated for each solution in the final generation.
#TODO: (optioneel) voorkomen dat we opnieuw de fitness moeten berekenen voor elke oplossing, duurt nml wat lang
fitness = ga.cal_pop_fitness(new_population)
# Then return the index of that solution corresponding to the best fitness.
best_match_idx = numpy.where(fitness == numpy.max(fitness))

print("Best solution : ", new_population[best_match_idx])
print("Best solution fitness : ", int(numpy.max(fitness)))
