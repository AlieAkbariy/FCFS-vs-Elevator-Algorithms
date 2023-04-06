import matplotlib.pyplot as plt
from ProjectPart2.Analysis import Analysis
import statistics


class Output:
    def __init__(self, path, starting_position, rotation_latency, transfer_time, seek_time):
        self.analysis = Analysis(rotation_latency, transfer_time, seek_time)

        self.analysis.start(path, starting_position)

    def plot_full_data(self):
        data = self.analysis.elevator_elements
        test_case = [i for i in range(len(data['time']))]
        plt.subplot(2, 4, 1)
        plt.title('Time')
        plt.xlabel('test_case')
        plt.ylabel('time(ms)')
        plt.plot(test_case, data['time'], color='b')
        avg = statistics.mean(data['time'])
        plt.axhline(avg, color='r', label='average')
        plt.legend()

        plt.subplot(2, 4, 2)
        plt.title('Change Direction')
        plt.xlabel('test_case')
        plt.ylabel('# Change Direction')
        plt.plot(test_case, data['change_direction'], color='b')
        avg = statistics.mean(data['change_direction'])
        plt.axhline(avg, color='r', label='average')
        plt.legend()

        plt.subplot(2, 4, 3)
        plt.title('Head Change')
        plt.plot(test_case, data['head_change'], color='b')
        avg = statistics.mean(data['head_change'])
        plt.axhline(avg, color='r', label='average')
        plt.legend()

        plt.subplot(2, 4, 4)
        plt.title('Starvation')
        plt.plot(test_case, data['starvation'], color='b')
        avg = statistics.mean(data['starvation'])
        plt.axhline(avg, color='r', label='average')
        plt.legend()

        data = self.analysis.fcfs_elements

        plt.subplot(2, 4, 5)
        plt.plot(test_case, data['time'], color='b')
        avg = statistics.mean(data['time'])
        plt.axhline(avg, color='r', label='average')
        plt.legend()

        plt.subplot(2, 4, 6)
        plt.plot(test_case, data['change_direction'], color='b')
        avg = statistics.mean(data['change_direction'])
        plt.axhline(avg, color='r', label='average')
        plt.legend()

        plt.subplot(2, 4, 7)
        plt.plot(test_case, data['head_change'], color='b')
        avg = statistics.mean(data['head_change'])
        plt.axhline(avg, color='r', label='average')
        plt.legend()

        plt.subplot(2, 4, 8)
        plt.plot(test_case, data['starvation'], color='b')
        avg = statistics.mean(data['starvation'])
        plt.axhline(avg, color='r', label='average')
        plt.legend()

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
