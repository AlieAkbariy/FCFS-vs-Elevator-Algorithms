def add_action():
    global action_list

    num = len(req_time)

    for i in range(num):
        if time < req_time[0][1]:
            return

        action_list.append(req_time.pop(0))


def do_action():
    global time, start_pos, serviced_req

    try:
        if action_list[0][1] <= time:
            action = action_list.pop(0)
            if action[0] - start_pos == 0:
                time += R + T
            else:
                time += (abs(action[0] - start_pos) / S) + R + T + 1
            start_pos = action[0]
            result.append([action[0], time])
            serviced_req += 1
    except:
        pass


if __name__ == '__main__':
    R = float(input('Rotation Latency: '))
    T = float(input('Transfer Time: '))
    S = float(input('Seek Time: '))
    start_pos = float(input('Starting Position: '))

    # R = 4.17
    # T = 0.13
    # S = 4000.0
    # start_pos = 8000.0

    req_time = [[8000, 0],
                [24000, 0],
                [56000, 0],
                [16000, 10],
                [64000, 20],
                [40000, 30]]

    result = []

    all_req = len(req_time)
    serviced_req = 0

    action_list = []

    time = 0

    while serviced_req != all_req:
        add_action()

        do_action()

    print('\nResult:\n')
    for r in result:
        print(r)
