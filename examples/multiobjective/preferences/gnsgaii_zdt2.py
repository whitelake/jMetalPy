from jmetal.algorithm.multiobjective.nsgaii import NSGAII

from jmetal.util.comparator import GDominanceComparator, RankingAndCrowdingDistanceComparator
from jmetal.operator import SBXCrossover, PolynomialMutation, BinaryTournamentSelection
from jmetal.problem import ZDT2, ZDT1
from jmetal.util.observer import VisualizerObserver, ProgressBarObserver
from jmetal.util.solution_list import print_function_values_to_file, print_variables_to_file, read_solutions
from jmetal.util.termination_criterion import StoppingByEvaluations
from jmetal.util.visualization import Plot

"""
.. module:: GNSGA-II
   :platform: Unix, Windows
   :synopsis: GNSGA-II (Non-dominance Sorting Genetic Algorithm II with preference articulation
   based on a reference point).

.. moduleauthor:: Antonio J. Nebro <antonio@lcc.uma.es>
"""

if __name__ == '__main__':
    problem = ZDT2()
    problem.reference_front = read_solutions(filename='../../../resources/reference_front/{}.pf'.format(problem.get_name()))

    reference_point = [0.5, 0.5]

    max_evaluations = 25000
    algorithm = NSGAII(
        problem=problem,
        population_size=100,
        offspring_population_size=100,
        mutation=PolynomialMutation(probability=1.0 / problem.number_of_variables, distribution_index=20),
        crossover=SBXCrossover(probability=1.0, distribution_index=20),
        selection=BinaryTournamentSelection(comparator=RankingAndCrowdingDistanceComparator()),
        dominance_comparator=GDominanceComparator(reference_point),
        termination_criterion=StoppingByEvaluations(max=max_evaluations)
    )

    algorithm.observable.register(observer=ProgressBarObserver(max=max_evaluations))

    algorithm.run()
    front = algorithm.get_result()

    # Plot front
    plot_front = Plot(plot_title='gNSGAII-ZDT1', axis_labels=problem.obj_labels, reference_point=reference_point, reference_front=problem.reference_front)
    plot_front.plot([algorithm.get_result()], labels=['Pareto front'], filename='gNSGAII-ZDT1.eps')

    # Save results to file
    print_function_values_to_file(front, 'FUN.' + algorithm.get_name() + "." + problem.get_name())
    print_variables_to_file(front, 'VAR.'+ algorithm.get_name() + "." + problem.get_name())

    print('Algorithm (continuous problem): ' + algorithm.get_name())
    print('Problem: ' + problem.get_name())
    print('Computing time: ' + str(algorithm.total_computing_time))