import matplotlib.pyplot as plt
import numpy as np
from ProjectPart2.Analysis import Analysis
import statistics


class Output:
    def __init__(self, path, starting_position, rotation_latency, transfer_time, seek_time):
        self.analysis = Analysis(rotation_latency, transfer_time, seek_time)

        self.analysis.start(path, starting_position)

    def plot_full_data(self):
        plt.figure('All Data Representation')
        data = self.analysis.elevator_elements
        test_case = [i for i in range(len(data['time']))]
        plt.subplot(3, 4, 1)
        plt.title('Time')
        plt.bar(test_case, data['time'], color='b')

        plt.subplot(3, 4, 2)
        plt.title('Change Direction')
        plt.bar(test_case, data['change_direction'], color='b')

        plt.subplot(3, 4, 3)
        plt.title('Head Change')
        plt.bar(test_case, data['head_change'], color='b')

        plt.subplot(3, 4, 4)
        plt.title('Starvation')
        plt.bar(test_case, data['starvation'], color='b')

        data = self.analysis.fcfs_elements

        plt.subplot(3, 4, 5)
        plt.bar(test_case, data['time'], color='b')

        plt.subplot(3, 4, 6)
        plt.bar(test_case, data['change_direction'], color='b')

        plt.subplot(3, 4, 7)
        plt.bar(test_case, data['head_change'], color='b')

        plt.subplot(3, 4, 8)
        plt.bar(test_case, data['starvation'], color='b')

        plt.subplot(3, 4, 9)
        plt.axhline(statistics.mean(self.analysis.elevator_elements['time']), color='b', label='elevator')
        plt.axhline(statistics.mean(self.analysis.fcfs_elements['time']), color='r', label='fcfs')
        plt.legend()

        plt.subplot(3, 4, 10)
        plt.axhline(statistics.mean(self.analysis.elevator_elements['change_direction']), color='b', label='elevator')
        plt.axhline(statistics.mean(self.analysis.fcfs_elements['change_direction']), color='r', label='fcfs')
        plt.legend()

        plt.subplot(3, 4, 11)
        plt.axhline(statistics.mean(self.analysis.elevator_elements['head_change']), color='b', label='elevator')
        plt.axhline(statistics.mean(self.analysis.fcfs_elements['head_change']), color='r', label='fcfs')
        plt.legend()

        plt.subplot(3, 4, 12)
        plt.axhline(statistics.mean(self.analysis.elevator_elements['starvation']), color='b', label='elevator')
        plt.axhline(statistics.mean(self.analysis.fcfs_elements['starvation']), color='r', label='fcfs')
        plt.legend()

        plt.figure('Compare Data')
        plt.subplot(1, 4, 1)
        plt.title('Time')
        plt.bar(test_case, np.subtract(np.array(self.analysis.fcfs_elements['time']),
                                       np.array(self.analysis.elevator_elements['time'])))

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
        plt.show()

        # elevator

        # axs[0, 1].plot(x, y)
        # axs[0, 1].set_title('head change')
        #
        # axs[0, 2].plot(x, y)
        # axs[0, 2].set_title('starvation')
        #
        # # fcfs
        # axs[1, 0].plot(x, y)
        # axs[1, 0].set_title('time')
        #
        # axs[1, 1].plot(x, y)
        # axs[1, 1].set_title('head change')
        #
        # axs[1, 2].plot(x, y)
        # axs[1, 2].set_title('starvation')

    def plot_compare_data(self):
        pass
