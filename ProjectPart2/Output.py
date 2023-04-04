import matplotlib.pyplot as plt
from ProjectPart2.Analysis import Analysis


class Output:
    def __init__(self, path, starting_position, rotation_latency, transfer_time, seek_time):
        self.analysis = Analysis(rotation_latency, transfer_time, seek_time)

        self.analysis.start(path, starting_position)

    def plot_full_data(self):
        fig, axs = plt.subplots(2, 3)

        # elevator
        axs[0, 0].plot(range(0, len(self.analysis.elements['elevator']['elevator_time']) - 1),
                       self.analysis.elements['elevator']['elevator_time'])
        axs[0, 0].set_title('time')

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
