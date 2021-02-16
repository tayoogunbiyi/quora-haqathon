from typing import List

class Test:
    def __init__(self, run_time: float, success_probability: float):
        self.run_time = run_time
        self.success_probability = success_probability
        self.weight = (1 - self.success_probability) / self.run_time

    def __str__(self) -> str:
        return f"Test(run_time={self.run_time},success_probability={self.success_probability}),weight={self.weight}"

    def __repr__(self) -> str:
        return self.__str__()

    def __lt__(self, other):
        return self.weight < other.weight

def read_input() -> List[Test]:
    input_lines = []
    while True:
        try:
            input_lines.append(input())
        except EOFError:
            break

    tests = []
    for line in input_lines[1:]:
        run_time, probability = line.strip().split(" ")
        run_time, probability = float(run_time), float(probability)

        tests.append(Test(run_time, probability))
    return tests


def compute_minimum_expected_time(tests: List[Test]):
    tests.sort(reverse=True)
    time_elapsed = 0
    current_probabilty = 1

    for i in range(len(tests)):
        time_elapsed += tests[i].run_time * current_probabilty
        current_probabilty *= tests[i].success_probability

    return time_elapsed


print(compute_minimum_expected_time(read_input()))