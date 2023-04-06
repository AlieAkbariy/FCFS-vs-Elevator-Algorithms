from ProjectPart2.GenerateDataset import Dataset
from ProjectPart2.Output import Output

if __name__ == '__main__':
    # a = Dataset('../dataset.xlsx', 3, 5)
    # a.generate()
    # b = Dataset.read_dataset('../dataset.xlsx')
    # for i in b:
    #     print(i)

    path = '../dataset.xlsx'
    # dataset = Dataset(path, 100, 5)
    # dataset.generate()
    rotation_latency, transfer_time, seek_time, starting_position = 4.17, 0.13, 4000.0, 8000

    output = Output(path, starting_position, rotation_latency, transfer_time, seek_time)

    output.plot_full_data()
