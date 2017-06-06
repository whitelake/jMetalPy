import threading
from typing import TypeVar, Generic, List

S = TypeVar('S')
R = TypeVar('R')


class Algorithm(Generic[S, R], threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.observable = None
        self.evaluations = 0

    def run(self):
        pass

    def get_name(self):
        pass


class EvolutionaryAlgorithm(Algorithm[S, R]):
    def __init__(self):
        super(EvolutionaryAlgorithm,self).__init__()
        self.population = []

    def create_initial_population(self) -> List[S]:
        pass

    def evaluate_population(self, population: List[S]) -> List[S]:
        pass

    def init_progress(self) -> None:
        pass

    def is_stopping_condition_reached(self) -> bool:
        pass

    def selection(self, population: List[S]) -> List[S]:
        pass

    def reproduction(self, population: List[S]) -> List[S]:
        pass

    def replacement(self, population: List[S], offspring_population: List[S]) -> List[S]:
        pass

    def update_progress(self):
        pass

    def get_result(self)->R:
        pass

    def run(self):
        self.population = self.create_initial_population()
        self.population = self.evaluate_population(self.population)
        self.init_progress()
        while not self.is_stopping_condition_reached():
            mating_population = self.selection(self.population)
            offspring_population = self.reproduction(mating_population)
            offspring_population = self.evaluate_population(offspring_population)
            self.population = self.replacement(self.population, offspring_population)
            self.update_progress()

