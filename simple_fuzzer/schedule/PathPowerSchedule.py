from typing import Dict, List, List
from .PowerSchedule import PowerSchedule
from utils.Seed import Seed
from utils.ObjectUtils import dump_object, load_object, get_md5_of_object
import os, random

class PathPowerSchedule(PowerSchedule):

    def __init__(self, some_parameter: int = 5) -> None:
        super().__init__()
        self.some_parameter = some_parameter
        self.path_frequency: Dict[str, int] = {}
        self.population_energy: Dict[Seed, float] = {}


    def assign_energy(self, population: List[Seed]) -> None:
        """Assign exponential energy inversely proportional to path frequency"""
        if not population:
            raise ValueError("Population is empty")

        for seed in population:
            path = seed.metadata.get('path', '')
            if path in self.path_frequency:
                self.path_frequency[path] += 1
            else:
                self.path_frequency[path] = 1

        for seed in population:
            path = seed.metadata.get('path', '')
            frequency = self.path_frequency.get(path, 1)
            # Assign energy inversely proportional to path frequency
            self.population_energy[seed] = 1.0 / frequency ** 0.5  # Using square root for exponential decay

        # Normalize energy to ensure sum of all energies is 1
        total_energy = sum(self.population_energy.values())
        if total_energy > 0:
            for seed in self.population_energy:
                self.population_energy[seed] /= total_energy
        else:
            raise ValueError("Total energy is zero after assignment. Check the population and path frequencies.")

    def choose(self, population: List[Seed]) -> Seed:
        if not population:
            raise ValueError("Population is empty")

        norm_energy = self.normalized_energy(population)
        if not norm_energy:
            raise ValueError("Normalized energy list is empty. Check the population and energy assignment.")
        
        seed: Seed = random.choices(population, weights=norm_energy)[0]
        return seed
