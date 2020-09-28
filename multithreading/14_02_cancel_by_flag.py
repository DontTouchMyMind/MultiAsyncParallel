import threading
import time

from multithreading.count_three_sum import read_ints

should_stop = False


def count_three_sum(ints, thread_name='t'):
    print(f'Started count_three_sum in {thread_name}')

    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if should_stop:
                    print('Task was cancelled')
                    counter = -1
                    return counter
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'Triple found in {thread_name}: {ints[i]}, {ints[j]}, {ints[k]}')

    print(f'Ended count_three_sum in {thread_name}. Triplets counter={counter}')
    return counter


if __name__ == '__main__':
    print('Started Main')

    ints = read_ints('../data/1Kints.txt')

    p = threading.Thread(target=count_three_sum, args=(ints,))
    p.start()

    time.sleep(5)

    should_stop = True
    time.sleep(2)

    print('Ended Main')