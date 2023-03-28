class Helper:
    @staticmethod
    def io_handler():
        starting_position = float(input("Enter Starting Position:"))
        number_of_request = int(input("Enter Number Of Request:"))
        requests = list()

        for i in range(number_of_request):
            request = input()
            request_list = request.split(' ')
            request_list[0] = int(request_list[0])
            request_list[1] = int(request_list[1])
            requests.append(request_list)

        return starting_position, requests
