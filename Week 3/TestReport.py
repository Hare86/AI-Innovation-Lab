
import numpy as np


class TestReport:
    def __init__(self, execution_times):
        self.execution_times = execution_times

    def average_time(self):
        return np.mean(self.execution_times)

    def max_time(self):
        return np.max(self.execution_times)


class RegressionReport(TestReport):
    def __init__(self, execution_times):
        super().__init__(execution_times)

    def slow_tests(self, threshold):
        return self.execution_times[self.execution_times > threshold]


if __name__ == "__main__":
    
    execution_times = np.array([1.2, 2.5, 0.9, 3.1, 2.0, 1.8, 2.7, 3.5, 1.1, 2.9])

    
    report = RegressionReport(execution_times)

    
    print("Average Execution Time:", report.average_time())
    print("Maximum Execution Time:", report.max_time())
    print("Slow Tests (threshold > 2.5):", report.slow_tests(2.5))
