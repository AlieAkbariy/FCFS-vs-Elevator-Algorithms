from ProjectPart1.Helper import Helper
from Algorithm.FirstComeFirstServiced import FirstComeFirstServiced
from Algorithm.ElevatorAlgorithm import Elevator

if __name__ == '__main__':
    starting_position, requests = Helper.io_handler()

    elevator = Elevator(4.17, 0.13, 4000.0, starting_position, requests.copy())
    print('-------------------------------------- Elevator Result -----------------------------------------')
    elevator.start()
    print('-------------------------------------- End Elevator Result -------------------------------------\n')

    first_come_first_serviced = FirstComeFirstServiced(4.17, 0.13, 4000.0, starting_position, requests.copy())
    print('-------------------------------------- FCFS Result ----------------------------------------------')
    first_come_first_serviced.start()
    print('-------------------------------------- End FCFS Result ------------------------------------------')
