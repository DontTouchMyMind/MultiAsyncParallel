import threading

from multithreading.count_three_sum import read_ints, count_three_sum
from multithreading.decorators import measure_time


@measure_time
def run_in_parallel(ints):
    t1 = threading.Thread(target=count_three_sum, daemon=True, args=(ints, 't1'))
    t2 = threading.Thread(target=count_three_sum, daemon=True, args=(ints, 't2'))

    t1.start()
    t2.start()

    print('\nGoing to wait for threads')

    t2.join()
    t2.join()


@measure_time
def run_in_sequentially(ints):
    count_three_sum(ints, 'main')
    count_three_sum(ints, 'main')


if __name__ == '__main__':
    print('Started main')

    ints = read_ints('../data/2Kints.txt')

    run_in_parallel(ints)  # Executed time is 271.11 seconds.
    run_in_sequentially(ints)  # Executed time is 266.25 seconds.

    print('Ended main')
