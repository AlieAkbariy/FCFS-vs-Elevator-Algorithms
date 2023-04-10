from ProjectPart2.GenerateDataset import Dataset
import os


class FullDatasetGenerator:
    def __init__(self, dir_name, test_case_number, request_num):
        self.dir_name = dir_name
        self.test_case_number = test_case_number
        self.request_num = request_num

    def start(self):
        path = f'../Datasets/{self.dir_name}/'
        if not os.path.exists(path):
            os.mkdir(path)
        file = open(path + "README.txt", "w")
        file.write("oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\n" +
                   f"Number Of Datasets:  {self.test_case_number}\n" +
                   f"Number Of Requests: {self.request_num}\n" +
                   "oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")

        dataset = Dataset(path + f'dataset.xlsx', self.test_case_number, self.request_num)
        dataset.generate()
