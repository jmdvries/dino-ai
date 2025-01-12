import numpy
import arcade
from dinogame.gamescreen import GameScreen
# This project is extended and a library called PyGAD is released to build the genetic algorithm.
# PyGAD documentation: https://pygad.readthedocs.io
# PyGAD source code at GitHub: https://github.com/ahmedfgad/GeneticAlgorithmPython


def cal_pop_fitness(pop):
    # make the solutions play the game
    fitness = numpy.empty(8)
    for idx, sol in enumerate(pop):
        # print(sol)
        game = GameScreen(AI=True, weights=sol)
        game.setup()
        arcade.run()
        # print(game.score)
        # idx = numpy.where(pop == sol)[0]
        fitness[idx] = game.score
        # fitness = numpy.sum(pop*equation_inputs, axis=1)
    print(fitness)
    return fitness


def select_mating_pool(pop, fitness, num_parents):
    # Selecting the best individuals in the current gen as parents for producing the offspring of the next generation
    parents = numpy.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = numpy.where(fitness == numpy.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999999
    print(parents)
    return parents


def crossover(parents, offspring_size):
    offspring = numpy.empty(offspring_size)
    # The point at which crossover takes place between two parents. Usually it is at the center.
    crossover_point = numpy.uint8(offspring_size[1]/2)

    for k in range(offspring_size[0]):
        # Index of the first parent to mate.
        parent1_idx = k % parents.shape[0]
        # Index of the second parent to mate.
        parent2_idx = (k+1) % parents.shape[0]
        # The new offspring will have its first half of its genes taken from the first parent.
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        # The new offspring will have its second half of its genes taken from the second parent.
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring


def mutation(offspring_crossover):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring_crossover.shape[0]):
        # The random value to be added to the gene.
        random_value = numpy.random.uniform(-1.0, 1.0, 1)
        random_gene = numpy.random.randint(0, 3)
        offspring_crossover[idx,
                            random_gene] = offspring_crossover[idx, random_gene] + random_value
    print("#offspring")
    print(offspring_crossover)
    return offspring_crossover
