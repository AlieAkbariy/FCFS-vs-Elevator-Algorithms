from Algorithm.ElevatorAlgorithm import Elevator
from Algorithm.FirstComeFirstServiced import FirstComeFirstServiced
from GenerateDataset import Dataset


class Analysis:

    def start(self, dataset_path, starting_position):
        requests_list = Dataset.read_dataset(dataset_path)

        for request_list in requests_list:
            elevator = Elevator(4.17, 0.13, 4000.0, starting_position, request_list.copy())
            fcfs = FirstComeFirstServiced(4.17, 0.13, 4000.0, starting_position, request_list.copy())

            elevator.start()
            fcfs.start()
            # todo: Save result to attribute of this class
