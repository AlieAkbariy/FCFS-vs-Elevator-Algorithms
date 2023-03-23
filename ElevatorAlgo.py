def add_action():
    global action_list_up, action_list_down, direction

    if direction == 0:
        try:
            if req_time[0][0] >= start_pos:
                direction = 1
            else:
                direction = -1
        except:
            pass

    num = len(req_time)

    for i in range(num):
        if time < req_time[0][1]:
            return

        if req_time[0][0] >= start_pos:
            action_list_up.append(req_time.pop(0))
        else:
            action_list_down.append(req_time.pop(0))

    action_list_up.sort(key=lambda row: (row[0]))
    action_list_down.sort(key=lambda row: (row[0]), reverse=True)


def do_action():
    global direction

    try:
        if direction == 1:
            if len(action_list_up) != 0:
                action_up()
            elif len(action_list_down) != 0:
                direction = -1
                action_down()

        else:
            if len(action_list_down) != 0:
                action_down()
            elif len(action_list_up) != 0:
                direction = 1
                action_up()
    except:
        pass


def action_up():
    global start_pos, time, serviced_req

    action = action_list_up.pop(0)
    if action[0] - start_pos == 0:
        time += R + T
    else:
        time += (abs(action[0] - start_pos) / S) + R + T + 1
    start_pos = action[0]
    result.append([action[0], time])
    serviced_req += 1


def action_down():
    global start_pos, time, serviced_req

    action = action_list_down.pop(0)
    if action[0] - start_pos == 0:
        time += R + T
    else:
        time += (abs(action[0] - start_pos) / S) + R + T + 1
    start_pos = action[0]
    result.append([action[0], time])
    serviced_req += 1


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

    direction = 0

    all_req = len(req_time)
    serviced_req = 0

    action_list_up = []
    action_list_down = []

    result = []

    time = 0

    while serviced_req != all_req:
        add_action()

        do_action()

    print('\nResult:\n')
    for r in result:
        print(r)
