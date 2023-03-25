from BaseAlgorithm import BaseAlgorithm


class Elevator(BaseAlgorithm):

    def __init__(self, rotation_latency, transfer_time, seek_time, starting_position, request_list):
        super().__init__(rotation_latency, transfer_time, seek_time, starting_position, request_list)
        self.action_list_up = list()
        self.action_list_down = list()
        self.direction = 0

    def add_action(self):
        if self.direction == 0:
            try:
                if self.request_list[0][0] >= self.starting_position:
                    self.direction = 1
                else:
                    self.direction = -1
            except Exception as ex:
                print(ex)

        num = len(self.request_list)

        for i in range(num):
            if self.time < self.request_list[0][1]:
                return

            if self.request_list[0][0] >= self.starting_position:
                self.action_list_up.append(self.request_list.pop(0))
            else:
                self.action_list_down.append(self.request_list.pop(0))

        self.action_list_up.sort(key=lambda row: (row[0]))
        self.action_list_down.sort(key=lambda row: (row[0]), reverse=True)

    def do_action(self):
        try:
            if self.direction == 1:
                if len(self.action_list_up) != 0:
                    self.__action_in(self.action_list_up)
                elif len(self.action_list_down) != 0:
                    self.direction = -1
                    self.__action_in(self.action_list_down)

            else:
                if len(self.action_list_down) != 0:
                    self.__action_in(self.action_list_down)
                elif len(self.action_list_up) != 0:
                    self.direction = 1
                    self.__action_in(self.action_list_up)
        except Exception as ex:
            print(ex)

    def __action_in(self, action_list):
        action = action_list.pop(0)
        reading_delay = self.rotation_latency + self.transfer_time
        start_stop_overhead = 1
        if action[0] - self.starting_position == 0:
            self.time += reading_delay
        else:
            self.time += (abs(action[0] - self.starting_position) / self.seek_time)
            self.time += reading_delay + start_stop_overhead
        self.starting_position = action[0]
        self.result.append([action[0], self.time])
        self.serviced_req += 1


# Test Algorithm
# a = Elevator(4.17, 0.13, 4000.0, 8000, [[8000, 0],
#                                         [24000, 0],
#                                         [56000, 0],
#                                         [16000, 10],
#                                         [64000, 20],
#                                         [40000, 30]])
# a.start()
