import matplotlib.pyplot as plt
import numpy as np
from ProjectPart2.Analysis import Analysis
import statistics


class Output:
    def __init__(self, path, starting_position, rotation_latency, transfer_time, seek_time):
        self.analysis = Analysis(rotation_latency, transfer_time, seek_time)

        self.analysis.start(path, starting_position)

    def plot_full_data(self):
        plt.figure('All Data Representation', figsize=(14, 7))
        data = self.analysis.elevator_elements
        test_case = [i for i in range(len(data['time']))]

        plt.subplot(2, 4, 1)
        plt.title('Time', fontsize=18)
        plt.bar(test_case, data['time'], color='b')
        plt.xlabel(f"< Avg: {statistics.mean(data['time'])} >", fontsize=12)
        plt.ylabel("Elevator", fontsize=18)

        plt.subplot(2, 4, 2)
        plt.title('Change Direction', fontsize=18)
        plt.bar(test_case, data['change_direction'], color='b')
        plt.xlabel(f"< Avg: {statistics.mean(data['change_direction'])} >", fontsize=12)

        plt.subplot(2, 4, 3)
        plt.title('Head Change', fontsize=18)
        plt.bar(test_case, data['head_change'], color='b')
        plt.xlabel(f"< Avg: {statistics.mean(data['head_change'])} >", fontsize=12)

        plt.subplot(2, 4, 4)
        plt.title('Starvation', fontsize=18)
        plt.bar(test_case, data['starvation'], color='b')
        plt.xlabel(f"< Avg: {statistics.mean(data['starvation'])} >", fontsize=12)

        data = self.analysis.fcfs_elements

        plt.subplot(2, 4, 5)
        plt.bar(test_case, data['time'], color='b')
        plt.xlabel(f"< Avg: {statistics.mean(data['time'])} >", fontsize=12)
        plt.ylabel("FCFS", fontsize=18)

        plt.subplot(2, 4, 6)
        plt.bar(test_case, data['change_direction'], color='b')
        plt.xlabel(f"< Avg: {statistics.mean(data['change_direction'])} >", fontsize=12)

        plt.subplot(2, 4, 7)
        plt.bar(test_case, data['head_change'], color='b')
        plt.xlabel(f"< Avg: {statistics.mean(data['head_change'])} >", fontsize=12)

        plt.subplot(2, 4, 8)
        plt.bar(test_case, data['starvation'], color='b')
        plt.xlabel(f"< Avg: {statistics.mean(data['starvation'])} >", fontsize=12)

        plt.tight_layout(pad=0.5)

        plt.show()

    def plot_compare_data(self):
        plt.figure('Compare Data', figsize=(14, 4))

        data = self.analysis.elevator_elements
        test_case = [i for i in range(len(data['time']))]

        plt.subplot(1, 4, 1)
        plt.title('Time')
        plt.bar(test_case, np.subtract(np.array(self.analysis.fcfs_elements['time']),
                                       np.array(self.analysis.elevator_elements['time'])))
        plt.ylabel("Data (FCFS - Elevator)", fontsize=18)

        plt.subplot(1, 4, 2)
        plt.title('Change Direction')
        plt.bar(test_case, np.subtract(np.array(self.analysis.fcfs_elements['change_direction']),
                                       np.array(self.analysis.elevator_elements['change_direction'])))

        plt.subplot(1, 4, 3)
        plt.title('Head Change')
        plt.bar(test_case, np.subtract(np.array(self.analysis.fcfs_elements['head_change']),
                                       np.array(self.analysis.elevator_elements['head_change'])))

        plt.subplot(1, 4, 4)
        plt.title('Starvation')
        plt.bar(test_case, np.subtract(np.array(self.analysis.fcfs_elements['starvation']),
                                       np.array(self.analysis.elevator_elements['starvation'])))

        plt.tight_layout(pad=0.5)

        plt.show()
