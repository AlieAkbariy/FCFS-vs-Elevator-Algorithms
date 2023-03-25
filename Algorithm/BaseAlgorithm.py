from abc import ABC, abstractmethod


class BaseAlgorithm(ABC):
    def __init__(self, rotation_latency, transfer_time, seek_time, starting_position, request_list):
        self.rotation_latency = rotation_latency
        self.transfer_time = transfer_time
        self.seek_time = seek_time
        self.starting_position = starting_position
        self.request_list = request_list

        self.result = list()
        try:
            self.req_number = len(self.request_list)
        except Exception as ex:
            self.req_number = 0

        self.serviced_req = 0
        self.action_list = list()
        self.time = 0

    @abstractmethod
    def add_action(self):
        pass

    @abstractmethod
    def do_action(self):
        pass

    def __print(self):
        print('\nResult:\n')
        for r in self.result:
            print(r)

    def start(self):
        while self.serviced_req != self.req_number:
            self.add_action()

            self.do_action()

        self.__print()
