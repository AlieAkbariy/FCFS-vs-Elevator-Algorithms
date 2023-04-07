import matplotlib.pyplot as plt
import numpy as np
from ProjectPart2.Analysis import Analysis
import statistics

import tableprint as tableprint


def print_table_results(elevator_results, fcfs_results):
    print('⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜')
    tableprint.table(elevator_results,
                     ['Elevator', 'AVG Time', 'AVG Change Direction', 'AVG Head Change', 'AVG Starvation'])
    print('⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜')

    tableprint.table(fcfs_results, ['FCFS', 'AVG Time', 'AVG Change Direction', 'AVG Head Change', 'AVG Starvation'])
    print('⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜')


def calc_results(num, data):
    return [num, statistics.mean(data['time']), statistics.mean(data['change_direction']),
            statistics.mean(data['head_change']), statistics.mean(data['starvation'])]


class CompareOutputs:
    def __init__(self, path, comparing_datas_id, starting_position, rotation_latency, transfer_time, seek_time):
        self.comparing_datas_id = comparing_datas_id
        self.path = path
        self.starting_position = starting_position
        self.analysis = Analysis(rotation_latency, transfer_time, seek_time)

    def start(self):
        elevator_results = []
        fcfs_results = []

        for i in self.comparing_datas_id:
            self.analysis.start(self.path + f'{i}/dataset.xlsx', self.starting_position)

            data_elevator = self.analysis.elevator_elements
            data_fcfs = self.analysis.fcfs_elements

            number_of_requests = len(self.analysis.requests_lists[0])

            elevator_results.append(calc_results(number_of_requests, data_elevator))
            fcfs_results.append(calc_results(number_of_requests, data_fcfs))

            self.analysis.requests_lists = None
            self.analysis.elements = dict()
            self.analysis.elevator_elements = dict()
            self.analysis.fcfs_elements = dict()

        print_table_results(elevator_results, fcfs_results)
