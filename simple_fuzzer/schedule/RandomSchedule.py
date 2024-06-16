import random
from typing import List
from .PowerSchedule import PowerSchedule
from utils.Seed import Seed

class RandomSchedule(PowerSchedule):

    def __init__(self) -> None:
        super().__init__()

    def assign_energy(self, population: List[Seed]) -> None:
        """Assign random energy to each seed"""
        population_size = len(population)
        if population_size == 0:
            return

        total_energy = 0.0
        for seed in population:
            energy = random.random()
            self.population_energy[seed] = energy
            total_energy += energy

        # Normalize energy to ensure sum of all energies is 1
        if total_energy > 0:
            for seed in self.population_energy:
                self.population_energy[seed] /= total_energy
