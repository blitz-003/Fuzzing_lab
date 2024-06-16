import time
from typing import Any, Tuple, List

from .GreyBoxFuzzer import GreyBoxFuzzer
from schedule.PathPowerSchedule import PathPowerSchedule
from runner.FunctionCoverageRunner import FunctionCoverageRunner

class PathGreyBoxFuzzer(GreyBoxFuzzer):
    """Count how often individual paths are exercised."""

    def __init__(self, seeds: List[str], schedule: PathPowerSchedule, is_print: bool):
        super().__init__(seeds, schedule, False)

        self.path_frequency = {}  # To track how often each path is taken
        self.start_time = time.time()
        self.last_crash_time = self.start_time
        self.is_print = is_print
        
        print("""
┌───────────────────────┬───────────────────────┬───────────────────────┬───────────────────┬───────────────────┬────────────────┬───────────────────┐
│        Run Time       │     Last New Path     │    Last Uniq Crash    │    Total Execs    │    Total Paths    │  Uniq Crashes  │   Covered Lines   │
├───────────────────────┼───────────────────────┼───────────────────────┼───────────────────┼───────────────────┼────────────────┼───────────────────┤""")
    
    def print_stats(self):
        def format_seconds(seconds):
            hours = int(seconds) // 3600
            minutes = int(seconds % 3600) // 60
            remaining_seconds = int(seconds) % 60
            return f"{hours:02d}:{minutes:02d}:{remaining_seconds:02d}"

        template = """│{runtime}│{path_time}│{crash_time}│{total_exec}│{total_path}│{uniq_crash}│{covered_line}│
├───────────────────────┼───────────────────────┼───────────────────────┼───────────────────┼───────────────────┼────────────────┼───────────────────┤"""
        template = template.format(runtime=format_seconds(time.time() - self.start_time).center(23),
                                   path_time="".center(23),
                                   crash_time=format_seconds(self.last_crash_time - self.start_time).center(23),
                                   total_exec=str(self.total_execs).center(19),
                                   total_path="".center(19),
                                   uniq_crash=str(len(set(self.crash_map.values()))).center(16),
                                   covered_line=str(len(self.covered_line)).center(19))
        print(template)

    def run(self, runner: FunctionCoverageRunner) -> Tuple[Any, str]:
        """Inform scheduler about path frequency"""
        result, outcome = super().run(runner)

        # Handle different outcomes
        if outcome == 'CRASH':
            self.last_crash_time = time.time()

        # Check if result is of expected type with coverage attribute
        if hasattr(result, 'coverage'):
            path = tuple(result.coverage)  # Using coverage as a proxy for path

            # Update path frequency
            if path in self.path_frequency:
                self.path_frequency[path] += 1
            else:
                self.path_frequency[path] = 1

        if self.is_print:
            self.print_stats()

        return result, outcome
