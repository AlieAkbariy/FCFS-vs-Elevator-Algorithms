from Algorithm.ElevatorAlgorithm import Elevator
from Algorithm.FirstComeFirstServiced import FirstComeFirstServiced
from GenerateDataset import Dataset


class Analysis:

    def __init__(self, rotation_latency, transfer_time, seek_time):
        self.rotation_latency = rotation_latency
        self.transfer_time = transfer_time
        self.seek_time = seek_time

        self.elements = dict()

        self.elevator_elements = dict()
        self.fcfs_elements = dict()

    def start(self, dataset_path, starting_position):
        requests_list = Dataset.read_dataset(dataset_path)

        elevator_time = []
        elevator_change_direction = []
        elevator_head_change = []
        elevator_starvation = []

        fcfs_time = []
        fcfs_change_direction = []
        fcfs_head_change = []
        fcfs_starvation = []

        for request_list in requests_list:
            elevator = Elevator(self.rotation_latency, self.transfer_time, self.seek_time, starting_position,
                                request_list.copy())
            fcfs = FirstComeFirstServiced(self.rotation_latency, self.transfer_time, self.seek_time, starting_position,
                                          request_list.copy())

            elevator.start()
            elevator_time.append(elevator.time)
            elevator_change_direction.append(elevator.direction_change)
            elevator_head_change.append(elevator.head_changing)
            elevator_starvation.append(self.__calc_starvation(elevator.result))

            fcfs.start()
            fcfs_time.append(fcfs.time)
            fcfs_change_direction.append(fcfs.direction_change)
            fcfs_head_change.append(fcfs.head_changing)
            fcfs_starvation.append(self.__calc_starvation(fcfs.result))

        self.elevator_elements = {'elevator_time': elevator_time,
                                  'elevator_change_direction': elevator_change_direction,
                                  'elevator_head_change': elevator_head_change,
                                  'elevator_starvation': elevator_starvation}

        self.fcfs_elements = {'fcfs_time': fcfs_time,
                              'fcfs_change_direction': fcfs_change_direction,
                              'fcfs_head_change': fcfs_head_change,
                              'fcfs_starvation': fcfs_starvation}

        self.elements['elevator'] = self.elevator_elements
        self.elements['fcfs'] = self.fcfs_elements

    def __calc_starvation(self, result):
        time = 0
        margin = self.rotation_latency + self.transfer_time

        for i in result:
            time += (i[2] - i[1] - margin)

        return time
