from typing import List
from .PowerSchedule import PowerSchedule
from utils.Seed import Seed

class RoundRobinSchedule(PowerSchedule):

    def __init__(self) -> None:
        super().__init__()
        self.current_index = 0

    def assign_energy(self, population: List[Seed]) -> None:
        
        population_size = len(population)
        if population_size == 0:
            return

        for seed in population:
            self.population_energy[seed] = 1.0 / population_size

        # Move to the next seed for the next round
        self.current_index = (self.current_index + 1) % population_size
