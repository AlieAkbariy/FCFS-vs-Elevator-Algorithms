from Algorithm.BaseAlgorithm import BaseAlgorithm


class FirstComeFirstServiced(BaseAlgorithm):

    def __init__(self, rotation_latency, transfer_time, seek_time, starting_position, request_list):
        super().__init__(rotation_latency, transfer_time, seek_time, starting_position, request_list)

        self.action_list = list()
        self.direction = 0

    def add_action(self):
        for i in range(len(self.request_list)):
            if self.time < self.request_list[0][1]:
                if len(self.action_list) == 0:
                    self.time = self.request_list[0][1]
                else:
                    return

            self.action_list.append(self.request_list.pop(0))

    def do_action(self):
        try:
            if self.action_list[0][1] <= self.time:
                action = self.action_list.pop(0)
                reading_delay = self.rotation_latency + self.transfer_time
                start_stop_overhead = 1

                if self.direction == 0:
                    if action[0] - self.starting_position >= 0:
                        self.direction = 1
                    else:
                        self.direction = -1

                if action[0] - self.starting_position == 0:
                    self.time += reading_delay
                else:
                    head_change = abs(action[0] - self.starting_position)
                    self.time += (head_change / self.seek_time)
                    self.time += reading_delay + start_stop_overhead

                    if self.direction == 1:
                        if action[0] - self.starting_position < 0:
                            self.direction = -1
                            self.direction_change += 1
                    elif self.direction == -1:
                        if action[0] - self.starting_position > 0:
                            self.direction = 1
                            self.direction_change += 1

                    self.head_changing += head_change

                self.starting_position = action[0]
                self.result.append([action[0], action[1], self.time])
                self.serviced_req += 1

        except Exception as ex:
            print(ex)

# Test Algorithm
# a = FirstComeFirstServiced(4.17, 0.13, 4000.0, 8000, [[8000, 0],
#                                                       [24000, 0],
#                                                       [56000, 0],
#                                                       [16000, 10],
#                                                       [64000, 20],
#                                                       [40000, 30],
#                                                       [50000, 90]])
# a.start()
