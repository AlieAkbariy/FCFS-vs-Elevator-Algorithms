from ProjectPart2.GenerateDataset import Dataset

if __name__ == '__main__':
    a = Dataset('../dataset.xlsx', 3, 3)
    a.generate()
    b = a.read_dataset()
    print(b)
