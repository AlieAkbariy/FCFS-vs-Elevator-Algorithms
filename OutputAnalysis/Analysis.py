from ProjectPart2.GenerateDataset import read_dataset


class Analysis:
    def __init__(self, data_path, number_of_datasets):
        self.data_path = data_path
        self.number_of_datasets = number_of_datasets
        self.elevator_data = []
        self.f_com_f_serv_data = []

    def start_analysis(self):
        for i in range(self.number_of_datasets):
            dataset = read_dataset(dataset_path=self.data_path + f'{i}')

            self.do_elevator_algo(dataset)
            self.f_com_f_serv_data(dataset)

    def do_elevator_algo(self, dataset):
        # todo : append to list
        pass

    def do_f_com_f_serv_algo(self, dataset):
        # todo : append to list
        pass

    def plot_data(self):
        pass

    def compare_data(self):
        pass
