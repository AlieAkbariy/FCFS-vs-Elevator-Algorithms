from ProjectPart2.GenerateDataset import Dataset


class FullDatasetGenerator:
    def __init__(self, dir_name, number_of_datasets, request_num):
        self.dir_name = dir_name
        self.number_of_datasets = number_of_datasets
        self.request_num = request_num

    def start(self):
        path = f'../Datasets/{self.dir_name}/'

        file = open(path + "README.txt", "w")
        file.write("oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\n" +
                   f"Number Of Datasets:  {self.number_of_datasets}\n" +
                   f"Number Of Requests: {self.request_num}\n" +
                   "oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")

        dataset = Dataset(path + f'dataset.xlsx', self.number_of_datasets, self.request_num)
        dataset.generate()
