import os
import time

from fuzzer.PathGreyBoxFuzzer import PathGreyBoxFuzzer
from runner.FunctionCoverageRunner import FunctionCoverageRunner
from schedule.PathPowerSchedule import PathPowerSchedule
from samples.Samples import sample1, sample2, sample3, sample4
from utils.ObjectUtils import dump_object, load_object


class Result:
    def __init__(self, coverage, crashes, start_time, end_time):
        self.covered_line = coverage
        self.crashes = crashes
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return "Covered Lines: " + str(self.covered_line) + ", Crashes Num: " + str(self.crashes) + ", Start Time: " + str(self.start_time) + ", End Time: " + str(self.end_time)


if __name__ == "__main__":

# #####################  Sample 1

#     f_runner = FunctionCoverageRunner(sample1)
#     seeds = load_object("corpus/corpus_1")

#     grey_fuzzer = PathGreyBoxFuzzer(seeds=seeds, schedule=PathPowerSchedule(5), is_print=True)
#     start_time = time.time()
#     grey_fuzzer.runs(f_runner, run_time=300)
#     res = Result(grey_fuzzer.covered_line, set(grey_fuzzer.crash_map.values()), start_time, time.time())
#     dump_object("_result" + os.sep + "Sample-1.pkl", res)
#     print(load_object("_result" + os.sep + "Sample-1.pkl"))

#####################  Sample 2



    f_runner = FunctionCoverageRunner(sample2)
    seeds = load_object("corpus/corpus_2")

    grey_fuzzer = PathGreyBoxFuzzer(seeds=seeds, schedule=PathPowerSchedule(10), is_print=True)
    start_time = time.time()
    grey_fuzzer.runs(f_runner, run_time=600)
    res = Result(grey_fuzzer.covered_line, set(grey_fuzzer.crash_map.values()), start_time, time.time())
    dump_object("_result" + os.sep + "Sample-2.pkl", res)
    print(load_object("_result" + os.sep + "Sample-2.pkl"))

# ################### Sample 3
#     f_runner = FunctionCoverageRunner(sample3)
#     seeds = load_object("corpus/corpus_3")

#     grey_fuzzer = PathGreyBoxFuzzer(seeds=seeds, schedule=PathPowerSchedule(10), is_print=True)
#     start_time = time.time()
#     grey_fuzzer.runs(f_runner, run_time=600)
#     res = Result(grey_fuzzer.covered_line, set(grey_fuzzer.crash_map.values()), start_time, time.time())
#     dump_object("_result" + os.sep + "Sample-3.pkl", res)
#     print(load_object("_result" + os.sep + "Sample-3.pkl"))


# ################### Sample 4
#     f_runner = FunctionCoverageRunner(sample4)
#     seeds = load_object("corpus/corpus_4")

#     grey_fuzzer = PathGreyBoxFuzzer(seeds=seeds, schedule=PathPowerSchedule(45), is_print=True)
#     start_time = time.time()
#     grey_fuzzer.runs(f_runner, run_time=2700)
#     res = Result(grey_fuzzer.covered_line, set(grey_fuzzer.crash_map.values()), start_time, time.time())
#     dump_object("_result" + os.sep + "Sample-4.pkl", res)
#     print(load_object("_result" + os.sep + "Sample-4.pkl"))


