from Algorithm.ElevatorAlgorithm import Elevator
from Algorithm.FirstComeFirstServiced import FirstComeFirstServiced
from GenerateDataset import Dataset


class Analysis:

    def __init__(self, rotation_latency, transfer_time, seek_time):
        self.rotation_latency = rotation_latency
        self.transfer_time = transfer_time
        self.seek_time = seek_time

        self.elevator_time = []
        self.elevator_change_direction = []
        self.elevator_head_change = []
        self.elevator_starvation = []

        self.fcfs_time = []
        self.fcfs_change_direction = []
        self.fcfs_head_change = []
        self.fcfs_starvation = []

    def start(self, dataset_path, starting_position):
        requests_list = Dataset.read_dataset(dataset_path)

        for request_list in requests_list:
            elevator = Elevator(self.rotation_latency, self.transfer_time, self.seek_time, starting_position,
                                request_list.copy())
            fcfs = FirstComeFirstServiced(self.rotation_latency, self.transfer_time, self.seek_time, starting_position,
                                          request_list.copy())

            elevator.start()
            self.elevator_time.append(elevator.time)
            self.elevator_change_direction.append(elevator.direction_change)
            self.elevator_head_change.append(elevator.head_changing)
            self.elevator_starvation.append(self.__calc_starvation(elevator.result))

            fcfs.start()
            self.fcfs_time.append(fcfs.time)
            self.fcfs_change_direction.append(fcfs.direction_change)
            self.fcfs_head_change.append(fcfs.head_changing)
            self.fcfs_starvation.append(self.__calc_starvation(fcfs.result))

    def __calc_starvation(self, result):
        time = 0
        margin = self.rotation_latency + self.transfer_time

        for i in result:
            time += (i[2] - i[1] - margin)

        return time
