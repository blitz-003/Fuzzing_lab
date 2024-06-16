import random
from typing import List, List

from utils.Seed import Seed

MAX_SEEDS = 1000


# PowerSchedule.py

# PowerSchedule.py

class PowerSchedule:
    def __init__(self):
        pass

    def normalized_energy(self, population):
        if not population:
            return []

        # Calculate sum of energy values
        sum_energy = sum([entry.energy for entry in population])

        if sum_energy == 0:
            # If sum of energy values is zero, initialize energies
            for entry in population:
                entry.energy = 1.0  # Adjust this initialization based on your requirements

            # Recalculate sum of energy values
            sum_energy = sum([entry.energy for entry in population])

        if sum_energy == 0:
            raise ValueError("Sum of energy values in population is still zero after initialization")

        # Calculate normalized energies
        norm_energy = [entry.energy / sum_energy for entry in population]

        return norm_energy

    def choose(self, population):
        norm_energy = self.normalized_energy(population)
        if not norm_energy:
            raise ValueError("Normalized energy list is empty. Check the population and energy assignment.")
        
        seed: Seed = random.choices(population, weights=norm_energy)[0]
        return seed
    
    def assign_energy(self, population: List[Seed]) -> None:
        """Assigns each seed the same energy"""
        for seed in population:
            seed.energy = 1


    
