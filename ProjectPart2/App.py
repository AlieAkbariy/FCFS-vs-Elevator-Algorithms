import os

from ProjectPart2.CompareOutputs import CompareOutputs
from ProjectPart2.FullDatasetGenerator import FullDatasetGenerator
from ProjectPart2.Output import Output


class App:
    def __init__(self):
        self.rotation_latency, self.transfer_time, self.seek_time, self.starting_position = 4.17, 0.13, 4000.0, 8000
        self.number_of_datasets = 0
        dataset_id = 1
        self.comparing_datas_id = []
        while os.path.exists(f'../Datasets/Dataset-{dataset_id}'):
            self.comparing_datas_id.append(dataset_id)
            dataset_id += 1

    def change_default_value(self):
        print("Hi let's change rotation latency, transfer time, seek time and starting position :)")
        self.rotation_latency = float(input("Rotation Latency: "))
        self.transfer_time = float(input("Transfer Time: "))
        self.seek_time = float(input("Seek Time: "))
        self.starting_position = float(input("Starting Position: "))

    def build_new_dataset(self):
        print('Generating new dataset! ')

        if not os.path.exists('../Datasets'):
            os.mkdir('../Datasets')

        self.number_of_datasets = int(input('How many dataset do you want to generate? '))
        for i in range(self.number_of_datasets):
            print(f'Generating dataset number {i + 1} .')
            number_of_test_case = int(input('Enter number of test case of this dataset:'))
            number_of_request = int(input('Enter number of request in each test case:'))
            data_set_name = f'Dataset-{i + 1}'
            FullDatasetGenerator(data_set_name, number_of_test_case, number_of_request).start()
            print(f'Dataset number {i + 1} created.\n')
            self.comparing_datas_id.append(i + 1)

    def plot_specific_dataset(self, dataset_id):
        path = f"../Datasets/Dataset-{dataset_id}/dataset.xlsx"
        if len(self.comparing_datas_id) == 0:
            print('Please create dataset first')
            return
        if dataset_id > self.comparing_datas_id[-1]:
            print('Invalid input')
            return
        output = Output(path, self.starting_position, self.rotation_latency, self.transfer_time, self.seek_time)
        output.plot_full_data()
        output.plot_compare_data()

    def calculate_avg_of_all_dataset_results(self):
        path = "../Datasets/Dataset-"
        CompareOutputs(path, self.comparing_datas_id, self.rotation_latency, self.transfer_time, self.seek_time,
                       self.starting_position).start()

    def start(self):
        while True:
            print('''
            1- Change default value of rotation latency, transfer time, seek time and starting position
            2- Generate Dataset
            3- Plot information for specific dataset
            4- Print result of all datasets
            5- Exit
            ''')

            user_input = input('>')
            if user_input == '1':
                self.change_default_value()
            elif user_input == '2':
                self.build_new_dataset()
            elif user_input == '3':
                dataset_id = int(input('Please enter data set id:'))
                self.plot_specific_dataset(dataset_id)
            elif user_input == '4':
                self.calculate_avg_of_all_dataset_results()
            elif user_input == '5':
                break
            else:
                print('Invalid input')
