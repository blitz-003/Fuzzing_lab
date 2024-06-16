from typing import List
from .PowerSchedule import PowerSchedule
from utils.Seed import Seed

class CoveragePowerSchedule(PowerSchedule):

    def __init__(self) -> None:
        super().__init__()

    def assign_energy(self, population: List[Seed]) -> None:
        """Assign energy based on the coverage provided by each seed"""
        total_coverage = 0.0
        coverage_map = {}

        for seed in population:
            coverage = len(seed.metadata.get('coverage', []))
            coverage_map[seed] = coverage
            total_coverage += coverage

        for seed in population:
            coverage = coverage_map.get(seed, 0)
            if total_coverage > 0:
                self.population_energy[seed] = coverage / total_coverage
            else:
                self.population_energy[seed] = 1.0 / len(population) if len(population) > 0 else 0
