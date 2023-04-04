from ProjectPart2.GenerateDataset import Dataset, read_dataset

if __name__ == '__main__':
    a = Dataset('../dataset.xlsx', 3, 5)
    a.generate()
    b = read_dataset('../dataset.xlsx')
    for i in b:
        print(i)
